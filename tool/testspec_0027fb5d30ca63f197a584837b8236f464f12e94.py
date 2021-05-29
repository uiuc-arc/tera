from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
from src.lib.TestSpec import Spec
import libraries

testspecs = [
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_fasttext.py".format(
            libraries.PROJECT_DIR),
        classname="TestFastTextModel",
        testname="test_sg_hs_training",
        params=[
            Param(
                name="param1",
                param_line=471,
                param_col=30,
                param_type=ParamType.CHAINS,
                default_val=5,
                value_range=[1,2,3,4,5]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_fasttext.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=494,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(overlap_count, 2)",
                args=[]
            )
        ],
        branchname="before_0027fb5d30ca63f197a584837b8236f464f12e94"
    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_fasttext.py".format(
            libraries.PROJECT_DIR),
        classname="TestFastTextModel",
        testname="test_cbow_neg_training",
        params=[
            Param(
                name="param1",
                param_line=533,
                param_col=30,
                param_type=ParamType.CHAINS,
                default_val=5,
                value_range=[1,2,3,4,5]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_fasttext.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=556,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(overlap_count, 2)",
                args=[]
            )
        ],
        branchname="before_0027fb5d30ca63f197a584837b8236f464f12e94"
    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_doc2vec.py".format(
            libraries.PROJECT_DIR),
        classname="TestDoc2VecModel",
        testname="test_dbow_neg",
        params=[
            Param(
                name="epochs",
                param_line=505,
                param_col=90,
                param_type=ParamType.ITER,
                default_val=20,
                value_range=[1, 20],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_doc2vec.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=373,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(f2_rank, 30)",
                args=[]
            )
        ],
        branchname="before_0027fb5d30ca63f197a584837b8236f464f12e94"
    )
    ]