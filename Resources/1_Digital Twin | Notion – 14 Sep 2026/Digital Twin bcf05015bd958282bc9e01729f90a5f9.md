# Digital Twin

[AI Agent Paper](Digital%20Twin/AI%20Agent%20Paper%2001305015bd9583fe9c158176ca3667c0.md)

Project Ideas that students can work on, feel free to discuss if you are interested any of the following project, you can also work a part of the project:

1. ***Multi-Stakeholder Policy Coordination in Multimodal Mobility Systems Using Agent-Based Simulation @August***

**Motivation:**

Urban mobility decisions involve competing interests among city authorities, service operators, and users. This study extends the DTUMOS simulation framework to include multi-agent negotiation, allowing different stakeholders to debate, propose, and refine mobility policies within a simulated decision process.

- [https://microsoft.ai/new/the-path-to-medical-superintelligence/](https://microsoft.ai/new/the-path-to-medical-superintelligence/)

**Focus**:

- Introduce stakeholder-specific agent roles with distinct goals and constraints
- Coordinate through negotiation to resolve conflicting preferences in policy design

**Key Components**:

- **Stakeholder Agent Modeling**
    - Define agents for city planners, private operators, and commuters
    - Assign constraints, utilities, and negotiation behaviors to each agent
- **Multimodal Mobility Simulation (DTUMOS-based)**
    - Simulate the outcome of proposed policies under conflicting agent preferences
    - Include shared mobility, paratransit, and demand-responsive services
- **Negotiation and Conflict Resolution Framework**
    - Implement structured dialogue or decision rules (e.g., voting, scoring, argumentation)
    - Explore both rule-based and LLM-based coordination strategies
- **Evaluation**
    - Measure policy convergence, fairness, and system efficiency
    - Compare individual-policy vs negotiated-policy outcomes
1. **Development of Multi‑Modal Transportation Capabilities and ETA Prediction for Multi‑Pick‑Drop Ride‑Sharing**

**Motivation:**

A multimodal transportation system uses two or more modes (walking, cycling, bus, rail, taxi, etc.) to move people or goods from door to door.  Such systems can reduce the reliance on private cars, cut congestion and pollution, and redistribute passengers across different modes.  However, achieving seamless multimodal journeys requires accurate Estimated Time of Arrival (ETA) predictions across modes and efficient ride‑sharing algorithms that can handle multiple pick‑up and drop‑off points.  Advanced AI and machine‑learning techniques like dynamic route optimization, predictive demand forecasting and multi‑rider matching can improve route planning, resource allocation and ride‑pooling.  This project aims to develop a multimodal ETA and ride‑sharing capability within a digital‑twin mobility simulator (such as DTUMOS) to enable efficient, user‑centric transport planning.

**Focus:**

- **Integrate multimodal transport layers:** Combine public transit schedules, road networks and shared‑mobility services within a simulation environment to support routing that spans buses, trains, bikes, and ride‑hail vehicles.
- **Multi‑destination ride‑sharing:** Extend path‑planning algorithms to schedule multiple pick‑up and drop‑off points for pooled rides while balancing detours and fairness among passengers.
- **ETA prediction:** Develop machine‑learning models that estimate door‑to‑door travel times across modes, considering real‑time traffic, transit delays and transfer times.
- **Dynamic dispatch and matching:** Implement real‑time ride‑matching and vehicle dispatch algorithms that pair riders with drivers based on location, direction and ETA. AI-driven dispatching and route optimization have been shown to reduce travel times and fuel consumption, and increase ride-hail revenue when combined with reinforcement-learning dispatch.

**Key Components:**

- **Data Integration:**
    - Collect and preprocess datasets for public transit schedules, road networks, real‑time traffic and shared mobility demand.
    - Incorporate geospatial (GIS) data to model transit hubs and accessibility.
    - Use historical trip records to train demand prediction and ETA models.
- **Multimodal Routing Engine:**
    - Build or adapt a routing algorithm (e.g., a multimodal A* search) that can plan routes across different transport modes, factoring in transfer times and service frequencies.
    - Evaluate alternative sequences of modes to find the fastest or most convenient routes.
- **ETA Prediction Model:**
    - Develop a deep‑learning model (e.g., LSTM or transformer) that predicts travel time segments for each leg of a multimodal journey.
    - Include features such as departure time, day of week, weather, and current congestion.
    - Train the model on historical data and validate predictions using metrics like mean absolute error.
- **Ride‑Sharing and Multi‑Pick‑Drop Planning:**
    - Implement a multi‑rider matching algorithm that groups riders traveling in similar directions to share a vehicle, balancing detour time and occupancy. Such algorithms can reduce vehicle use and emissions while maintaining reasonable travel times.
    - Integrate the matching algorithm with the routing engine to schedule multiple pick‑ups and drop‑offs within acceptable detour thresholds.
    - Incorporate dynamic route optimization that continuously adjusts the route using live traffic data.
- **Dynamic Dispatch and Pricing (Optional Extensions):**
    - Experiment with reinforcement-learning-based dispatching and pricing strategies to optimize driver‑rider matching and fare adjustments. AI‑based dispatching has been shown to increase ride‑hail platforms’ revenue and reduce wait times.
    - Evaluate the effect of surge pricing and demand‑responsive fares on system efficiency.
- **Evaluation:**
    - Simulate multimodal journeys under various demand scenarios in DTUMOS or a similar digital‑twin environment.
    - Assess the accuracy of ETA predictions and their impact on rider satisfaction and system efficiency.
    - Compare multi‑pick‑drop ride‑sharing against single‑rider services in terms of travel time, vehicle utilization and emissions.
1. Multi-threaded programming to enhance the scalability of the DTUMOS: 
CPU‑bound simulations like DTUMOS do not benefit from Python’s `threading` library. I think 
by adopting **multiprocessing or compiled extensions**, the DTUMOS project can overcome current scalability limitations and deliver faster, more responsive simulations. @sulaiman

2. **EV Charging in DTUMOS**

Digital Twin for Urban Mobility Systems (DTUMOS) provides a virtual replica of urban transport infrastructure, integrating EV fleets, charging stations, and passenger demand. Efficient operation of EV fleets requires solving interconnected problems of **charging schedule optimization**, **fleet relocation**, and **dispatching strategies**. These modules, though distinct, must be coordinated to ensure system reliability, passenger satisfaction, and energy efficiency.

---

### Problem Modules

1. **Battery Management System (BMS) and Charging Schedule Optimization**
    - **Core Question**: *When and where should EVs charge, given demand forecasts and fleet utilization?*
    - Students will design algorithms that dynamically schedule charging based on:
        - Predicted passenger demand (spatiotemporal).
        - Energy availability at charging stations.
        - Vehicle state of charge (SoC) and charging speed.
    - The solution should balance charging needs with service availability, preventing overloading of infrastructure.
    - **Broader Impact**: Directly affects fleet size requirements and ensures sustainable operation.
2. **Vehicle Relocation for Demand Matching**
    - **Core Question**: *How can autonomous empty vehicles be re-positioned efficiently to meet future passenger demand?*
    - Students will create strategies for relocating idle EVs in anticipation of demand hotspots.
    - Relocation must account for:
        - Travel distance and energy consumption.
        - Station capacity and charging needs.
        - Demand prediction accuracy.
    - **Broader Impact**: Supports optimal fleet distribution and reduces passenger wait times.
3. **Fleet Dispatching and Operations (Optimization & Control)**
    - **Core Question**: *How should EVs be assigned to passengers in real-time while balancing operational costs and service quality?*
    - Students will use **Operations Research (OR) tools** (linear programming, mixed integer programming, heuristics, etc.) to design dispatch algorithms.
    - Must coordinate with charging and relocation decisions to ensure:
        - Efficient passenger pick-ups.
        - Energy-aware dispatching (e.g., avoiding assigning nearly-depleted vehicles).
    - **Broader Impact**: Lays foundation for **ride-sharing control**, demand-responsive transit, and fleet cost optimization.

---

### Interconnections

- **Modules 2 and 3 (Relocation + Dispatch)** depend on real-time demand forecasting.
- **Module 1 (Charging/BMS)** strongly influences both relocation and dispatch, as charging availability constrains fleet movement.
- Collectively, these modules contribute to **fleet size optimization** and **ride-sharing strategy design**.

---

### Student Research Directions

- Develop **algorithms** (heuristics, optimization, ML-based, or hybrid).
- Simulate scenarios using DTUMOS framework (with real or synthetic mobility data).
- Compare trade-offs between:
    - Passenger satisfaction (wait times).
    - Energy efficiency (charging loads, idle movement).
    - Operational cost (fleet size, utilization).

Most important Papers to study

1. [Optimizing Electric Vehicles Charging using Large Language Models and Graph Neural Networks](https://arxiv.org/html/2502.03067v1#:~:text=Maintaining%20grid%20stability%20amid%20widespread,research%20directions%20and%20innovative%20solutions)
2. [A Comprehensive Survey of Electric Vehicle Charging Demand Forecasting Techniques | IEEE Journals & Magazine | IEEE Xplore](https://ieeexplore.ieee.org/document/10670452)
3. [Scalable ride-matching and dispatching model for shared autonomous electric vehicles with real-time demand prediction - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0360835225005650?via%3Dihub)
4. [Scalable order dispatching through Federated Multi-Agent Deep Reinforcement Learning - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0957417424026599?via%3Dihub)

## Literature Review:

Most important Papers to study

1. https://doi.org/10.1038%2Fs41598-023-32326-9 
2. [https://microsoft.ai/new/the-path-to-medical-superintelligence/](https://microsoft.ai/new/the-path-to-medical-superintelligence/)
3. code: ‣ & ‣ (Updated version)

***(optional):***

1. [**STGformer: Efficient Spatiotemporal Graph Transformer for Traffic Forecasting**](https://arxiv.org/abs/2410.00385)
    1. https://github.com/Dreamzz5/STGformer
2. [**TransETA: transformer networks for estimated time of arrival with local congestion representation**](https://link.springer.com/article/10.1007/s10489-023-05139-6)

## Dataset

1. **Datasets for training ETA Models (We need GPS Dataset)**
    1. Porto Taxi Dataset.
        1. https://www.kaggle.com/datasets/crailtap/taxi-trajectory
        2. https://www.kaggle.com/c/pkdd-15-taxi-trip-time-prediction-ii
    2. Per-second GPS data from taxis in Sungnam, South Korea
        1. The data is currently being processed (Could share samples after preprocessing)
    3. Uber - DeepETA: https://www.uber.com/en-KR/blog/deepeta-how-uber-predicts-arrival-times/
    4. Google Deepmind: https://deepmind.google/discover/blog/traffic-prediction-with-advanced-graph-neural-networks/

## Important Links

1. Graph Neural Network
    1. https://github.com/GraphAlgoX/GraphMM-Master
    2. https://github.com/PacktPublishing/Hands-On-Graph-Neural-Networks-Using-Python
    3. https://github.com/amirerf/Spatio_temporal_data_analysis_with_Python
    4. https://medium.com/@ellenebay88/building-a-spatio-temporal-gcnn-model-for-traffic-incident-forcasting-using-arcpy-and-pytorch-3ae15edb7a6f
    5. https://towardsdatascience.com/graph-convolutional-networks-introduction-to-gnns-24b3f60d6c95/#:~:text=As%20deep%20learning%20models%20designed%20to%20process%20data,as%20the%20most%20prevalent%20and%20broadly%20applied%20model.
    6. https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/06-graph-neural-networks.html
    7. [Data Structures - Torch Spatiotemporal](https://torch-spatiotemporal.readthedocs.io/en/latest/usage/data_structures.html)
    8. https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/3eb41e58-0bae-47cf-aa47-fcf1608acc62/content#:~:text=In%20this%20thesis%2C%20we%20first%20introduce%20some%20mathematical,Neural%20Networks%2C%20Graph%20Attention%20Networks%2C%20GraphSAGE%2C%20and%20PinSAGE. 

### Other Digital Twins:

1. [Purdue Digital Twin Lab](https://purduedigitaltwin.github.io/)
2. https://abstreet.uk/projects/npw/
3. [a-b-street/abstreet: Transportation planning and traffic simulation software for creating cities friendlier to walking, biking, and public transit](https://github.com/a-b-street/abstreet)