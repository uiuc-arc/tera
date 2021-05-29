from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
from src.lib.TestSpec import Spec
import libraries

testspecs = [

    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/sbiutils_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_conditional_corrcoeff[0.99]",
        params=[
            Param(
                name="resolution",
                param_line=171,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[10, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/sbi/tests/sbiutils_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=174,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert torch.abs(corr - estimated_corr) < 1e-3",
                args=[]
            )
        ],
        branchname="before_39d6954c6073dc15aa1abe1d99589b15798e4901"
    ),
        Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/sbiutils_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_conditional_corrcoeff[0.95]",
        params=[
            Param(
                name="resolution",
                param_line=171,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[10, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/sbi/tests/sbiutils_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=174,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert torch.abs(corr - estimated_corr) < 1e-3",
                args=[]
            )
        ],
        branchname="before_39d6954c6073dc15aa1abe1d99589b15798e4901"
    ),
        Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/sbiutils_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_conditional_corrcoeff[0.0]",
        params=[
            Param(
                name="resolution",
                param_line=171,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[10, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/sbi/tests/sbiutils_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=174,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert torch.abs(corr - estimated_corr) < 1e-3",
                args=[]
            )
        ],
        branchname="before_39d6954c6073dc15aa1abe1d99589b15798e4901"
    ),

]
