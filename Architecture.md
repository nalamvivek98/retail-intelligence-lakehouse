          Source Platforms
 ┌────────────────────────────────┐
 │ Blinkit │ Instamart │ BB │ FK │
 └────────────────────────────────┘
                  ↓

         Ingestion Layer
      Python API Collectors
                  ↓

          Raw Data Store
         Bronze Delta Layer
                  ↓

       Spark Transformation
     Cleaning + Normalization
                  ↓

         Silver Delta Layer
       Unified Product Model
                  ↓

        Analytics Processing
     Pricing + Delivery KPIs
                  ↓

          Gold Delta Layer
        Business Intelligence
                  ↓

        Airflow Orchestration
    Scheduling + Monitoring



    grocery-price-platform/
│
├── airflow/
│   ├── dags/
│   └── logs/
│
├── ingestion/
│   ├── blinkit/
│   ├── instamart/
│   └── bigbasket/
│
├── spark_jobs/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── delta_tables/
│
├── configs/
│
├── monitoring/
│
├── tests/
│
├── docker/
│
├── docs/
│
└── README.md