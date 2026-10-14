# 📊 Gig-Economy-Game-Theory-Simulation

> **An Computational Microeconomic Simulation of Algorithmic Incentives, Spatial Congestion, and Worker Welfare in Two-Sided Platform Markets.**

---

## 📌 Executive Summary & Abstract

This project develops an agent-based economic simulation in Python to model the dynamic spatial-temporal interactions between ride-hailing/delivery platforms and gig workers under algorithmic dynamic pricing and location-based dynamic subsidies.

By integrating **Microeconomic Surplus Analysis**, **Sequential Non-Cooperative Games (Stackelberg Framework)**, and **Multi-Agent Decision Processes**, this repository simulates how decentralized workers optimize their labor supply decisions under spatial congestion externalities and shifting platform commission structures.

---

## 🧠 Theoretical Framework & Economic Modeling

### 1. Expected Driver Utility Function

Each individual driver agent $i$ decides whether to accept an order, stay, or relocate to grid cell $g$ based on the following expected net utility function:

$$EU_i(g,t) = p_i(g,t) \cdot R_i(g,t) - C(d) - w_i^{\text{res}} \cdot T_i(g,t) - \kappa_i(n_g)$$

Where:
- $p_i(g,t)$: Probability of receiving and completing an order in grid $g$ at time $t$, modeled as $p(g,t) = \min\left(1, \frac{D_{g,t}}{N_{g,t}}\right)$.
- $R_i(g,t)$: Expected payout conditional on order completion.
- $C(d)$: Operational marginal cost associated with travel distance $d$ (Deadhead distance).
- $w_i^{\text{res}}$: Driver's opportunity cost of time (Reservation wage per time unit).
- $T_i(g,t)$: Expected time committed, including transit and waiting time.
- $\kappa_i(n_g)$: Congestion externality penalty driven by driver concentration $n_g$.

---

### 2. Stackelberg Game Formulation (Platform & Workers)

The interaction is modeled as a multi-stage sequential game:

1. **Stage 1 — Platform (Leader):** Observes predicted market state $\hat{D}_{g,t}$ and sets spatial surge multipliers $S_{g,t}$ or location-based subsidies $b_{g,t}$ subject to a budget constraint:
   $$\Pi_t = \text{Commission Revenue}_t - \sum_g b_{g,t} Q_{g,t} \ge 0$$
2. **Stage 2 — Workers (Followers):** Observe spatial payout signals, update expected utility $EU_i(g,t)$, and independently select spatial actions or logout.
3. **Stage 3 — Market Clearing:** Matching algorithm executes; realized driver welfare, consumer surplus, and spatial demand mismatches update system states.

---

## 🔬 Experimental Architecture & Simulation Design

### 1. Spatial Grid Setup
- **Environment:** $10 \times 10$ discrete spatial matrix ($N = 100$ cells).
- **Demand Heterogeneity:**
  - **High-Demand Core ($3 \times 3$ Hotspot):** Generates **80%** of total stochastic order demand.
  - **Suburbs (Remaining 91 cells):** Generates **20%** of order demand.
- **Dynamic Demand Generator:** Injects stochastic orders into the grid per time step.

---

### 2. Experimental Scenarios (Counterfactual Analysis)

We simulate and compare three distinct market mechanisms:

#### 🔴 Scenario A: Uncoordinated Myopic Driver Choice (Baseline)
- **Mechanism:** Drivers operate purely under myopic local greedy heuristics based on historical demand signals, ignoring dynamic congestion costs.
- **Outcome:** Severe spatial supply-demand mismatch and driver over-clustering at core hotspots.

#### 🔵 Scenario B: Location-Based Dynamic Incentives (Treatment)
- **Mechanism:** The platform algorithmically injects dynamic subsidies $b_{g,t}$ into low-supply/high-demand grid locations based on real-time driver-to-order ratios:
  $$b_{g,t} = \min\left(b_{\max}, \lambda \cdot \max\left(0, \frac{\hat{D}_{g,t} - N_{g,t}}{\max(1, \hat{D}_{g,t})}\right)\right)$$
- **Outcome:** Improved spatial dispersion of supply matching actual spatial demand proportions.

#### 🟡 Scenario C: Dynamic Surge Pricing Benchmark
- **Mechanism:** Dynamic customer price adjustments influencing both demand elasticity and driver compensation.

---

### 📈 Primary Research Hypotheses & Evaluation Metrics

1. **$H_1$ (Market Efficiency):** Dynamic subsidies significantly increase overall **Order Completion Rate ($CR$)**:
   $$CR = \frac{\text{Completed Orders}}{\text{Generated Orders}}$$

2. **$H_2$ (Spatial Alignment):** Subsidies minimize the **Spatial Mismatch Index ($M_t$)**:
   $$M_t = \frac{1}{2} \sum_{g=1}^{100} \left\vert{} \frac{N_{g,t}}{N_t} - \frac{D_{g,t}}{D_t} \right\vert{}$$

3. **$H_3$ (Welfare Distribution):** Evaluates mean net driver utility $\bar{U}$, consumer surplus, and net platform profitability $\Pi_t$ post-subsidy expenditure.

4. **$H_4$ (Equilibrium Approximation):** Evaluates approximate Nash Stability via empirical regret metrics ($\epsilon_t$).

---

## 💻 Tech Stack & Simulation Architecture

- **Language:** Python 3.10+
- **Core Libraries:** `numpy`, `pandas`, `scipy`
- **Visualization Suite:** `matplotlib`, `seaborn`
- **Simulation Paradigm:** Agent-Based Modeling (ABM) / Monte Carlo Paired Replications
