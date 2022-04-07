import builtins
from constructs import Construct

from aws_cdk import aws_glue_alpha as glue


class ETLJob(Construct):
    def __init__(
        self, scope: Construct, id_: builtins.str, script_path: builtins.str
    ) -> None:
        super().__init__(scope, id_)

        glue.Job(
            self,
            "SparkETLJob",
            executable=glue.JobExecutable.python_etl(
                glue_version=glue.GlueVersion.V3_0,
                python_version=glue.PythonVersion.THREE,
                script=glue.Code.from_asset(script_path),
            ),
            description="Python Streaming Job",
        )
