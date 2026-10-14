# 📊 Gig-Economy-Game-Theory-Simulation

> **An Empirical & Computational Microeconomic Analysis of Algorithmic Pricing and Worker Decision-Making in Two-Sided Platform Markets.**

---

## 📌 Executive Summary & Abstract

This project develops an agent-based economic simulation in Python to model the dynamic interactions between ride-hailing/delivery platforms and gig platform workers under algorithmic dynamic pricing (surge pricing).

By integrating **Microeconomic Surplus Analysis**, **Sequential Non-Cooperative Games**, and **Markov Decision Processes (MDP)**, this repository simulates how workers optimize their labor supply decisions under information asymmetry and shifting platform commission structures.

---

## 🧠 Theoretical Framework & Economic Modeling

### 1. Driver Utility Function

Each individual driver agent $i$ decides whether to accept an order or move to a grid cell based on the following net utility function:

$$U_i = R - C(d) - \Theta(n)$$

Where:
- $R$: Expected revenue from completing the ride/order.
- $C(d)$: Marginal operational cost as a function of travel distance $d$ (Deadhead distance).
- $\Theta(n)$: Congestion externality penalty, driven by driver concentration $n$ in the local grid cell:
  $$\Theta(n) \propto \frac{n}{t_{\text{wait}}}$$

### 2. Game-Theoretic Formulation (Extensive Form Game)
The interaction between the Platform (Player 1) and the Collective Gig Workers (Player 2) is modeled as a multi-stage sequential game:

1. **Stage 1 (Platform):** Sets dynamic multiplier $S_t \in [1.0, 3.5]$ based on estimated real-time consumer demand $\hat{D}_t$.
2. **Stage 2 (Workers):** Observe localized expected payout and decide whether to **[Log In / Accept]** or **[Log Off / Reject]** based on reservation wage $w^{res}_i$.
3. **Stage 3 (Market Equilibrium):** Market clears; price elasticity of supply $\epsilon_s$ updates the matching algorithm.

---

## 🛠️ Key Features & Technical Architecture

- **Simulated Economic Environment:** Agent-based model representing heterogeneous driver preferences and spatial demand shifts.
- **Game-Theoretic Equilibrium Solvers:** Empirical calculation of Nash Equilibrium and Sequential Subgame Perfect Equilibrium (SPE).
- **Visualization Suite:** Dynamic plotting of driver surplus, platform revenue, and market clearing price paths using `matplotlib` and `seaborn`.

## 🔬 Experimental Architecture & Simulation Design

### 1. Grid Environment Setup
- **Spatial Grid:** $10 \times 10$ discrete spatial grid ($N = 100$ cells).
- **Demand Distribution:**
  - **High-Demand Hotspot ($3 \times 3$ Core Grid):** Generates **80%** of total order demand.
  - **Low-Demand Suburbs (Remaining 91 cells):** Generates **20%** of total order demand.
- **Dynamic Demand Generator:** Injects 100 stochastic orders/rides into the grid per time step.

---

### 2. Experimental Scenarios (Counterfactual Analysis)

We simulate and compare two distinct market clearing mechanisms:

#### 🔴 Baseline Scenario: Greedy Nash Equilibrium
- **Mechanism:** Drivers operate purely under local greedy strategies without dynamic price signals.
- **Behavior:** Drivers independently flock to the $3 \times 3$ Hotspot based on historic demand, ignoring cumulative congestion costs.
- **Outcome:** High congestion externalities, increased driver waiting times, and spatial supply-demand mismatch in suburban areas.

#### 🔵 Treatment Scenario: Dynamic Tip Subsidies (Dynamic Price Signals)
- **Mechanism:** The platform algorithmically injects dynamic tip/subsidy signals into low-supply/high-demand grid locations based on the real-time **Driver-to-Order Ratio**.
- **Behavior:** Decentralized drivers re-evaluate their expected net utility incorporating the dynamic price signal and redistribute spatially.
- **Outcome:** Optimal spatial dispersion of driver supply across the $10 \times 10$ environment.

---

### 📈 Expected Results & Evaluation Metrics

1. **Order Completion Rate (Market Efficiency):**
   - Evaluates total fulfilled orders / generated orders across time steps.
   - **Hypothesis:** Dynamic tip subsidies will significantly boost completion rates by incentivizing drivers to service suburban orders.

2. **Average Driver Utility & Platform Revenue:**
   - Measures net driver welfare ($\bar{U}$) and platform throughput.
   - **Hypothesis:** Reduction in congestion externalities at hotspots will increase average net driver utility.

3. **Welfare Distribution (Consumer & Supply Surplus):**
   - Quantifies total economic surplus gains generated under dynamic pricing intervention.

4. **Spatial Convergence Analysis (Statistical Proof):**
   - Applies spatial variance and distribution metrics (e.g., Chi-Square / Normal Distribution tests) to statistically demonstrate driver transition from **highly clustered aggregation** to a **balanced spatial equilibrium**.
