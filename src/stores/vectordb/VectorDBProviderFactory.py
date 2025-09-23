from .providers.QdrantDB import QdrantDBProvider
from .VectorDBEnums import VectorDBEnums
from controllers.BaseController import BaseController

class VectorDBProviderFactory:
    def __init__(self, config):
        self.config = config
        self.base_controller = BaseController()

    def create(self, provider: str):
        # 1. QDRANT.value لازم تتأكد انه Enum فيه .value او تستخدم Enum نفسه
        # 2. get_database_path: هل فعلا بياخد db_name؟ الاسم يوحي انه مسار مش اسم قاعدة بيانات
        # 3. لو فيه Providers تانية لازم تضيفهم هنا
        # 4. لو config مش فيه VECTOR_DB_PATH او VECTOR_DB_DISTANCE_METHOD هيحصل AttributeError
        # 5. الافضل raise Exception لو provider مش مدعوم بدل ما ترجع None (حسب استخدامك)
        if provider == VectorDBEnums.QDRANT.value:
            db_path = self.base_controller.get_database_path(db_name=self.config.VECTOR_DB_PATH)
            return QdrantDBProvider(
                db_path=db_path,
                distance_method=self.config.VECTOR_DB_DISTANCE_METHOD,
            )
        return None