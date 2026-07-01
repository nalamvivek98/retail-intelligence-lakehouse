Sprint 1


retail-intelligence-lakehouse/

├── airflow/
│
├── configs/
│   ├── app_config.yaml
│   ├── bigbasket.yaml
│   └── logging.yaml
│
├── docs/
│
├── ingestion/
│   ├── base/
│   │   └── base_ingestor.py
│   │
│   ├── sources/
│   │   └── bigbasket_ingestor.py
│   │
│   ├── models/
│   │   └── product.py
│   │
│   ├── utils/
│   │   ├── config_loader.py
│   │   ├── logger.py
│   │   └── retry_handler.py
│   │
│   └── orchestrator.py
│
├── raw/
│
├── spark_jobs/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── tests/
│
├── requirements.txt
│
└── README.md