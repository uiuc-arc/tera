from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
from src.lib.TestSpec import Spec
import libraries

testspecs = [Spec(
    repo="numpyro",
    filename="{0}/projects/numpyro/test/test_mcmc.py".format(
        libraries.PROJECT_DIR),
    classname="none",
    testname="test_compile_warmup_run[False-sequential-2]",
    params=[
        Param(
            name="num_samples",
            param_line=596,
            param_col=18,
            param_type=ParamType.ITER,
            default_val=10,
            value_range=[1, 20],
            steps=1
        ),
        Param(
            name="num_warmup",
            param_line=594,
            param_col=15,
            param_type=ParamType.ITER,
            default_val=10,
            value_range=[1, 20],
            steps=1
        )
    ],
    assertions=[
        AssertSpec(
            test=Test(testname="none",
                      classname="none",
                      filename="{0}/projects/numpyro/test/test_mcmc.py".format(
                          libraries.PROJECT_DIR)
                      ),
            line=609,
            col_offset=-1,
            assert_type=AssertType.ASSERT_ALLCLOSE,
            assert_string="assert_allclose(actual_samples, expected_samples)",
            args=[]
        )
    ],
    branchname="before_956789be0fc09b81d769a647d67e5ec303a50224"
)]
