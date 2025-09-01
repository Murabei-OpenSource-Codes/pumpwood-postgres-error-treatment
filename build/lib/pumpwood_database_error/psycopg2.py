"""Main module to treat psycopg2 errors."""
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool


class TreatPsycopg2Error:
    """Class to convert psycopg2 associated errors to normalized dictionary."""

    @classmethod
    def treat(cls, error: psycopg2.Error, connection_url: str = None) -> dict:
        """Main class to treat psycopg2 errors.

        Args:
            error (psycopg2.Error):
                Generic psycopg2 to be converted to dictionary.

        Returns:
            Return a dictionary with
        """
        # Create the engine with NullPool
        engine = create_engine(connection_url, poolclass=NullPool)

        message = str(error)
        print("message:", message)

        return {
            "message": message,
            "type": "PumpWoodDatabaseError",
            "payload": {}
        }


    # @app.errorhandler(psycopg2.errors.OperationalError)
    # def handle_psycopg2_operationalerror(error):
    #     pump_exc = exceptions.PumpWoodDatabaseError(message=str(error))
    #     response = jsonify(pump_exc.to_dict())
    #     response.status_code = pump_exc.status_code
    #     return response
    #
    # @app.errorhandler(psycopg2.errors.NotSupportedError)
    # def handle_psycopg2_notsupportederror(error):
    #     pump_exc = exceptions.PumpWoodDatabaseError(message=str(error))
    #     response = jsonify(pump_exc.to_dict())
    #     response.status_code = pump_exc.status_code
    #     return response
    #
    # @app.errorhandler(psycopg2.errors.ProgrammingError)
    # def handle_psycopg2_programmingerror(error):
    #     pump_exc = exceptions.PumpWoodDatabaseError(message=str(error))
    #     response = jsonify(pump_exc.to_dict())
    #     response.status_code = pump_exc.status_code
    #     return response
    #
    # @app.errorhandler(psycopg2.errors.DataError)
    # def handle_psycopg2_dataerror(error):
    #     pump_exc = exceptions.PumpWoodDatabaseError(message=str(error))
    #     response = jsonify(pump_exc.to_dict())
    #     response.status_code = pump_exc.status_code
    #     return response
    #
    # @app.errorhandler(psycopg2.errors.IntegrityError)
    # def handle_psycopg2_integrityerror(error):
    #     pump_exc = exceptions.PumpWoodDatabaseError(message=str(error))
    #     response = jsonify(pump_exc.to_dict())
    #     response.status_code = pump_exc.status_code
    #     return response
