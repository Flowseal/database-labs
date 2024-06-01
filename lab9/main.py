import models
import datetime
from sqlalchemy import create_engine, inspect, select, func
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///mydb.sqlite", echo=True)
models.Base.metadata.create_all(bind=engine)

inspector = inspect(engine)
schema_names = inspector.get_schema_names()
table_names = []

if __name__ == "__main__":
    for schema in schema_names:
      table_names += inspector.get_table_names(schema=schema)

    print("Available tables:\n- " + "\n- ".join(table_names))
    
    with Session(engine) as session:
      print("\n")

      my_flat = models.Flat(
         number="101b",
         rooms=2,
         square_area=23.4
      )
      other_flat = models.Flat(
         number="105",
         rooms=3,
         square_area=33.2
      )
      session.add_all([my_flat, other_flat])

      utility_service_water = models.UtilityServiceType(
          name="water"
      )
      utility_service_electricity = models.UtilityServiceType(
          name="electricity"
      )
      utility_service_light = models.UtilityServiceType(
          name="light"
      )
      session.add_all([utility_service_water, utility_service_electricity, utility_service_light])

      stmt = select(models.UtilityServiceType).where(models.UtilityServiceType.name == "light")
      light_service_type = session.scalars(stmt).one()
      light_service_type.name = "liiiight"

      stmt = select(models.UtilityServiceType)
      for service_type in session.scalars(stmt):
         print(service_type)

      session.delete(light_service_type)

      stmt = select(models.UtilityServiceType).where(models.UtilityServiceType.name == "water")
      water_service_type = session.scalars(stmt).one()
      utility_rate_water = models.UtilityRate(
         date_start=datetime.datetime.now(),
         date_end=datetime.datetime.now() + datetime.timedelta(days=14),
         price=1.05,
         service_type_id=water_service_type.id
      )  

      stmt = select(models.UtilityServiceType).where(models.UtilityServiceType.name == "electricity")
      electricity_service_type = session.scalars(stmt).one()
      utility_rate_electricity = models.UtilityRate(
         date_start=datetime.datetime.now(),
         date_end=datetime.datetime.now() + datetime.timedelta(days=14),
         price=0.88,
         service_type_id=electricity_service_type.id
      )

      session.add_all([utility_rate_water, utility_rate_electricity])

      payment1 = models.Payment(
        payment_amount=10.0,
        date=datetime.datetime.now(),
        flat_id=my_flat.id,
        utility_rate_id=utility_rate_water.id
      )
      payment2 = models.Payment(
        payment_amount=15.0,
        date=datetime.datetime.now(),
        flat_id=my_flat.id,
        utility_rate_id=utility_rate_electricity.id
      )
      payment3 = models.Payment(
        payment_amount=20.0,
        date=datetime.datetime.now(),
        flat_id=other_flat.id,
        utility_rate_id=utility_rate_water.id
      )

      session.add_all([payment1, payment2, payment3])
      
      # query = select([
      #     models.Flat,
      #     func.count(models.Flat.payments)
      # ]).group_by(models.Flat.payments)

      # result = engine.execute(query).fetchall()
 
      # # print all the records
      # for i in result:
      #     print("\n", i)

      session.commit()