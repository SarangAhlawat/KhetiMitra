from sqlalchemy import Column, Integer, Float, ForeignKey

from app.models.base import Base

class SustainabilityScore(Base):

    __tablename__ = "sustainability_scores"

    score_id = Column(Integer, primary_key=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.farm_id")
    )

    soil_score = Column(Float)

    water_score = Column(Float)

    chemical_score = Column(Float)

    biodiversity_score = Column(Float)

    economic_score = Column(Float)

    qssm_score = Column(Float)


QSSM_INDICATORS = {

    "soil_health": [

        "ph",

        "organic_carbon_percent",

        "nitrogen_kg_per_ha",

        "phosphorus_kg_per_ha",

        "potassium_kg_per_ha",

        "fertility_score"
    ],

    "water": [

        "rainfall",

        "water_stress_index",

        "annual_recharge_mcm",

        "annual_extraction_mcm",

        "extraction_percent"
    ],

    "chemical": [

        "nitrogen_kg_per_ha",

        "phosphorus_kg_per_ha",

        "potassium_kg_per_ha"
    ],

    "biodiversity": [

        "fertility_score",

        "climate_stress_score"
    ],

    "economic": [

        "yield_kg_per_ha",

        "production_tonnes",

        "area_hectares"
    ]
}