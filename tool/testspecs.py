from src.lib.AssertSpec import AssertSpec
from src.lib.AssertType import AssertType
from src.lib.Param import Param
from src.lib.ParamType import ParamType
from src.lib.Test import Test
from src.lib.TestSpec import Spec
import libraries

testspecs = [

    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianChainTests",
        testname="test_elbo_reparameterized_N_is_8",
        params=[
            Param(
                name="num_steps",
                param_line=113,
                param_col=32,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),
            Param(
                name="learning-rate",
                param_line=113,
                param_col=38,
                param_type=ParamType.LR,
                default_val=0.0015,
                value_range=[0.0001, 0.1]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=179,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_errors[0], prec=0.03)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianPyramidTests",
        testname="test_elbo_reparameterized_four_layers",
        params=[
            Param(
                name="num_steps",
                param_line=247,
                param_col=32,
                param_type=ParamType.ITER,
                default_val=20000,
                value_range=[100, 20000]
            ),
            Param(
                name="learning-rate",
                param_line=247,
                param_col=39,
                param_type=ParamType.LR,
                default_val=0.0015,
                value_range=[0.0001, 0.1]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=482,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_log_sig_error, prec=0.04)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
            libraries.PROJECT_DIR),
        classname="PoissonGammaTests",
        testname="test_mmd_vectorized",
        params=[
            Param(
                name="num_steps",
                param_line=291,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),
            Param(
                name="learning-rate",
                param_line=353,
                param_col=33,
                param_type=ParamType.LR,
                default_val=0.0002,
                value_range=[0.00001, 0.1]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=375,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(pyro.param('alpha_q'), self.alpha0, prec=0.2, msg='{} vs {}'.format())",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianPyramidTests",
        testname="test_elbo_nonreparameterized_three_layers",
        params=[
            Param(
                name="num_steps",
                param_line=257,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=15000,
                value_range=[100, 15000]
            ),
            Param(
                name="learning-rate",
                param_line=257,
                param_col=40,
                param_type=ParamType.LR,
                default_val=0.001,
                value_range=[0.0001, 0.1]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=482,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_log_sig_error, prec=0.04)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
            libraries.PROJECT_DIR),
        classname="NormalNormalTests",
        testname="test_mmd_nonvectorized",
        params=[
            Param(
                name="num_steps",
                param_line=98,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="learning-rate",
                param_line=163,
                param_col=33,
                param_type=ParamType.LR,
                default_val=0.001,
                value_range=[0.0001, 0.1]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=187,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, loc_error, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianPyramidTests",
        testname="test_elbo_reparameterized_three_layers",
        params=[
            Param(
                name="num_steps",
                param_line=241,
                param_col=32,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="learning-rate",
                param_line=241,
                param_col=39,
                param_type=ParamType.LR,
                default_val=0.0015,
                value_range=[0.0001, 0.1]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=482,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_log_sig_error, prec=0.04)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_tracegraph_elbo.py".format(
            libraries.PROJECT_DIR),
        classname="RaoBlackwellizationTests",
        testname="test_plate_in_elbo_with_superfluous_rvs",
        params=[
            Param(
                name="num_steps",
                param_line=405,
                param_col=86,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),
            Param(
                name="learning-rate",
                param_line=470,
                param_col=30,
                param_type=ParamType.LR,
                default_val=0.0012,
                value_range=[0.0001, 0.1]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_tracegraph_elbo.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=495,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, loc_error, prec=0.04)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianChainTests",
        testname="test_elbo_reparameterized_N_is_3",
        params=[
            Param(
                name="num_steps",
                param_line=109,
                param_col=32,
                param_type=ParamType.ITER,
                default_val=4000,
                value_range=[100, 4000]
            ),
            Param(
                name="learning-rate",
                param_line=109,
                param_col=38,
                param_type=ParamType.LR,
                default_val=0.0015,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=179,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_errors[0], prec=0.03)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianChainTests",
        testname="test_elbo_reparameterized_N_is_17",
        params=[
            Param(
                name="num_steps",
                param_line=119,
                param_col=32,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),
            Param(
                name="learning-rate",
                param_line=119,
                param_col=38,
                param_type=ParamType.LR,
                default_val=0.0015,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=179,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_errors[0], prec=0.03)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianChainTests",
        testname="test_elbo_nonreparameterized_N_is_3",
        params=[
            Param(
                name="num_steps",
                param_line=123,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),
            Param(
                name="learning-rate",
                param_line=123,
                param_col=39,
                param_type=ParamType.LR,
                default_val=0.001,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=179,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_errors[0], prec=0.04)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianChainTests",
        testname="test_elbo_nonreparameterized_N_is_5",
        params=[
            Param(
                name="num_steps",
                param_line=127,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),
            Param(
                name="learning-rate",
                param_line=127,
                param_col=39,
                param_type=ParamType.LR,
                default_val=0.001,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=179,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_errors[0], prec=0.06)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianChainTests",
        testname="test_elbo_nonreparameterized_N_is_7",
        params=[
            Param(
                name="num_steps",
                param_line=133,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),
            Param(
                name="learning-rate",
                param_line=133,
                param_col=39,
                param_type=ParamType.LR,
                default_val=0.001,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=179,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_errors[0], prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianPyramidTests",
        testname="test_elbo_nonreparameterized_two_layers",
        params=[
            Param(
                name="num_steps",
                param_line=253,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=8000,
                value_range=[100, 8000]
            ),
            Param(
                name="learning-rate",
                param_line=253,
                param_col=39,
                param_type=ParamType.LR,
                default_val=0.001,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=482,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_log_sig_error, prec=0.04)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianPyramidTests",
        testname="test_elbo_nonreparameterized_two_layers_model_permuted",
        params=[
            Param(
                name="num_steps",
                param_line=261,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="learning-rate",
                param_line=261,
                param_col=40,
                param_type=ParamType.LR,
                default_val=0.0007,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=482,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_log_sig_error, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
            libraries.PROJECT_DIR),
        classname="GaussianPyramidTests",
        testname="test_elbo_nonreparameterized_three_layers_model_permuted",
        params=[
            Param(
                name="num_steps",
                param_line=267,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=15000,
                value_range=[100, 15000]
            ),
            Param(
                name="learning-rate",
                param_line=267,
                param_col=40,
                param_type=ParamType.LR,
                default_val=0.0007,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/integration_tests/test_conjugate_gaussian_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=482,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(0.0, max_log_sig_error, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
            libraries.PROJECT_DIR),
        classname="PoissonGammaTests",
        testname="test_elbo_nonreparameterized",
        params=[
            Param(
                name="num_steps",
                param_line=274,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),
            Param(
                name="learning-rate",
                param_line=316,
                param_col=33,
                param_type=ParamType.LR,
                default_val=0.0002,
                value_range=[0.00005, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=322,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(pyro.param('alpha_q'), self.alpha_n, prec=0.2, msg='{} vs {}'.format(pyro.param('alpha_q').detach().cpu().numpy(), self.alpha_n.detach().cpu().numpy()))",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
            libraries.PROJECT_DIR),
        classname="PoissonGammaTests",
        testname="test_renyi_nonreparameterized",
        params=[
            Param(
                name="num_steps",
                param_line=280,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=12500,
                value_range=[100, 12500]
            ),
            Param(
                name="learning-rate",
                param_line=316,
                param_col=33,
                param_type=ParamType.LR,
                default_val=0.0002,
                value_range=[0.0001, 0.05]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=322,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(pyro.param('alpha_q'), self.alpha_n, prec=0.2, msg='{} vs {}'.format(pyro.param('alpha_q').detach().cpu().numpy(), self.alpha_n.detach().cpu().numpy()))",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_elbo_mapdata[iplate-8]",
        params=[
            Param(
                name="num_steps",
                param_line=50,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=7000,
                value_range=[100, 7000]
            ),
            Param(
                name="learning-rate",
                param_line=89,
                param_col=29,
                param_type=ParamType.LR,
                default_val=0.0008,
                value_range=[0.0001, 0.05]
            ),
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=109,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(loc_error.item(), 0, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_elbo_mapdata[iplate-None]",
        params=[
            Param(
                name="num_steps",
                param_line=50,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=7000,
                value_range=[100, 7000]
            ),
            Param(
                name="learning-rate",
                param_line=89,
                param_col=29,
                param_type=ParamType.LR,
                default_val=0.0008,
                value_range=[0.0001, 0.05]
            ),
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=109,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(loc_error.item(), 0, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_elbo_mapdata[range-3]",
        params=[
            Param(
                name="num_steps",
                param_line=50,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=7000,
                value_range=[100, 7000]
            ),
            Param(
                name="learning-rate",
                param_line=89,
                param_col=29,
                param_type=ParamType.LR,
                default_val=0.0008,
                value_range=[0.0001, 0.05]
            ),
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=109,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(loc_error.item(), 0, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_elbo_mapdata[range-8]",
        params=[
            Param(
                name="num_steps",
                param_line=50,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=7000,
                value_range=[100, 7000]
            ),
            Param(
                name="learning-rate",
                param_line=89,
                param_col=29,
                param_type=ParamType.LR,
                default_val=0.0008,
                value_range=[0.0001, 0.05]
            ),
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=109,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(loc_error.item(), 0, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pyro",
        filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_elbo_mapdata[range-None]",
        params=[
            Param(
                name="num_steps",
                param_line=50,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=7000,
                value_range=[100, 7000]
            ),
            Param(
                name="learning-rate",
                param_line=89,
                param_col=29,
                param_type=ParamType.LR,
                default_val=0.0008,
                value_range=[0.0001, 0.05]
            ),
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyro/tests/infer/test_elbo_mapdata.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=109,
                col_offset=-1,
                assert_type=AssertType.PYRO_ASSERT_EQUAL,
                assert_string="assert_equal(loc_error.item(), 0, prec=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 22
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_distributions.py".format(
            libraries.PROJECT_DIR),
        classname="TestMatchesScipy",
        testname="test_t",
        skip=True,
        params=[
            Param(
                name="num_samples",
                param_line=471,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_distributions.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=476,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="assert_almost_equal(dist.logcdf(value).tag.test_value, scipy_cdf,decimal=6, err_msg=str(pt))",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_distributions.py".format(
            libraries.PROJECT_DIR),
        classname="TestMatchesScipy",
        testname="test_beta",
        skip=True,
        params=[
            Param(
                name="num_samples",
                param_line=471,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_distributions.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=476,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="assert_almost_equal(dist.logcdf(value).tag.test_value, scipy_cdf,decimal=6, err_msg=str(pt))",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_mixture.py".format(
            libraries.PROJECT_DIR),
        classname="TestMixture",
        testname="test_mixture_list_of_normals",
        params=[
            Param(
                name="num_samples",
                param_line=78,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[1000, 5000]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_mixture.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=81,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(np.sort(trace['w'].mean(axis=0)),np.sort(self.norm_w),rtol=0.1, atol=0.1)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_fit_oo[SVGD-mini]",
        params=[
            Param(
                name="num_samples",
                param_line=708,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="learning-rate",
                param_line=683,
                param_col=58,
                param_type=ParamType.LR,
                default_val=0.075,
                value_range=[0.0001, 0.5]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=711,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(np.mean(trace['mu']), mu_post, rtol=0.05)",
                args=[]
            )
        ]
    ),
    # MXNET specs  ======================================================================
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_optimizer.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_sparse_adam",
        skip=True,
        params=[
            Param(
                name="param1",
                param_line=368,
                param_col=37,
                param_type=ParamType.LR,
                default_val=0.001,
                value_range=[0.001, 0.1]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/python/mxnet/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=2281,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="assert_almost_equal(t1, t2, rtol=rtol, atol=atol)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_random.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_randint_generator",
        skip=True,
        params=[
            Param(
                name="param1",
                param_line=1007,
                param_col=40,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            ),
            Param(
                name="param3",
                param_line=1013,
                param_col=109,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[100, 1000000]
            ),
            Param(
                name="param4",
                param_line=1020,
                param_col=119,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[100, 1000000]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/python/mxnet/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=2264,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (nrepeat*success_rate <= success_num)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_numpy_op.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_np_randint",
skip=True,
        params=[
            Param(
                name="nrepeat",
                param_line=3277,
                param_col=95,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            ),
            Param(
                name="nsamples1",
                param_line=3279,
                param_col=109,
                param_type=ParamType.ITER,
                default_val=1000000,
                value_range=[100, 1000000]
            ),
            Param(
                name="nsamples2",
                param_line=3286,
                param_col=119,
                param_type=ParamType.ITER,
                default_val=1000000,
                value_range=[100, 1000000]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/python/mxnet/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=2264,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (nrepeat*success_rate <= success_num)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_numpy_gluon.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_symbolic_basic_slicing",
        skip=True,
        params=[
            Param(
                name="param1",
                param_line=300,
                param_col=23,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/python/mxnet/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=2553,
                col_offset=-1,
                # this is a custom function that they use
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_almost_equal(saved_out_np, numpy_out, rtol=0.0001, atol=0.0001)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_poisson_nllloss_mod",
skip=True,
        params=[
            Param(
                name="param1",
                param_line=455,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=20,
                value_range=[1, 20]
            ),
            Param(
                name="param3",
                param_line=455,
                param_col=72,
                param_type=ParamType.LR,
                default_val=0.01,
                value_range=[0.001, 0.1]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=458,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (mod.score(data_iter, eval_metric=mx.metric.Loss())[0][1] < 0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_ctc_loss_train",
skip=True,
        params=[
            Param(
                name="param1",
                param_line=224,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200]
            ),
            Param(
                name="param2",
                param_line=224,
                param_col=73,
                param_type=ParamType.LR,
                default_val=0.01,
                value_range=[0.005, 0.1]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=227,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (mod.score(data_iter, eval_metric=mx.metric.Loss())[0][1] < 10)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_bce_loss_with_pos_weight",
skip=True,
        params=[
            Param(
                name="param1",
                param_line=476,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200]
            ),
            Param(
                name="param2",
                param_line=476,
                param_col=73,
                param_type=ParamType.LR,
                default_val=0.01,
                value_range=[0.005, 0.1]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=479,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (mod.score(data_iter, eval_metric=mx.metric.Loss())[0][1] < 0.01)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_triplet_loss",
skip=True,
        params=[
            Param(
                name="param1",
                param_line=346,
                param_col=33,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200]
            ),
            Param(
                name="param2",
                param_line=346,
                param_col=73,
                param_type=ParamType.LR,
                default_val=0.01,
                value_range=[0.005, 0.1]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/tests/python/unittest/test_loss.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=349,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (mod.score(data_iter, eval_metric=mx.metric.Loss())[0][1] < 0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_optimizer.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_signum",
        skip=True,
        params=[
            Param(
                name="param1",
                param_line=541,
                param_col=36,
                param_type=ParamType.LR,
                default_val=0.05,
                value_range=[0.01, 0.1]
            ),
            Param(
                name="param2",
                param_line=541,
                param_col=60,
                param_type=ParamType.LR,
                default_val=0.01,
                value_range=[0.01, 0.5]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/python/mxnet/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=2281,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="assert_almost_equal(t1, t2, rtol=rtol, atol=atol)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_optimizer.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_sparse_adagrad",
        skip=True,
        params=[
            Param(
                name="param2",
                param_line=763,
                param_col=37,
                param_type=ParamType.LR,
                default_val=0.01,
                value_range=[0.001, 0.01]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/python/mxnet/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=2281,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="assert_almost_equal(t1, t2, rtol=rtol, atol=atol)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="mxnet",
        filename="{0}/projects/mxnet/tests/python/unittest/test_optimizer.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_sparse_ftrl",
        skip=True,
        params=[
            Param(
                name="param1",
                param_line=613,
                param_col=50,
                param_type=ParamType.LR,
                default_val=0.1,
                value_range=[0.01, 0.5]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/mxnet/python/mxnet/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=2281,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="assert_almost_equal(t1, t2, rtol=rtol, atol=atol)",
                args=[]
            )
        ]
    ),

    # pymc3 again
    Spec(  # 37
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_step.py".format(
            libraries.PROJECT_DIR),
        classname="TestStepMethods",
        testname="test_step_continuous",
        params=[
            Param(
                name="draws",
                param_line=556,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=0,
                value_range=[1, 8000]
            ),
            Param(
                name="tune",
                param_line=557,
                param_col=21,
                param_type=ParamType.ITER,
                default_val=8000,
                value_range=[100, 8000]
            ),
            Param(
                name="chains",
                param_line=558,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=1,
                value_range=[1, 2, 3, 4, 5, 6]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_step.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=532,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string=" assert (np.abs(s[i]-value[i]) < bound[i])",
                args=[]
            )
        ]
    ),
    Spec(  # 38
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_data_container.py".format(
            libraries.PROJECT_DIR),
        classname="TestData",
        testname="test_sample_after_set_data",
        params=[
            Param(
                name="draws",
                param_line=80,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="tune",
                param_line=80,
                param_col=44,
                param_type=ParamType.ITER,
                default_val=8000,
                value_range=[1000, 8000]
            ),
            Param(
                name="chains",
                param_line=80,
                param_col=57,
                param_type=ParamType.CHAINS,
                default_val=1,
                value_range=[1, 2, 3, 4, 5, 6]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_data_container.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=90,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(new_y, pp_trace['obs'].mean(axis=0), atol=0.1)",
                args=[]
            )
        ]
    ),
    Spec(  # 39
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_step.py".format(
            libraries.PROJECT_DIR),
        classname="TestStepMethods",
        testname="test_step_categorical",
        params=[
            Param(
                name="draws",
                param_line=592,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=8000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=592,
                param_col=38,
                param_type=ParamType.ITER,
                default_val=0,
                value_range=[1, 8000]
            ),
            Param(
                name="chains",
                param_line=592,
                param_col=85,
                param_type=ParamType.CHAINS,
                default_val=1,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_step.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=532,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (np.abs(s[i]-value[i]) < bound[i])",
                args=[]
            )
        ]
    ),
    Spec(  # 40 # consider whether to include or exclude
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_data_container.py".format(
            libraries.PROJECT_DIR),
        classname="TestData",
        testname="test_sample_posterior_predictive_after_set_data",
        params=[
            Param(
                name="draws",
                param_line=63,
                param_col=30,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="tune",
                param_line=63,
                param_col=41,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[500, 8000]
            ),
            Param(
                name="chains",
                param_line=63,
                param_col=54,
                param_type=ParamType.CHAINS,
                default_val=1,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_data_container.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=71,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(x_test, y_test['obs'].mean(axis=0), atol=1e-1)",
                args=[]
            )
        ]
    ),
    Spec(  # 41
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_fit_oo[SVGD-full]",
        params=[
            Param(
                name="num_samples",
                param_line=708,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="learning-rate",
                param_line=679,
                param_col=58,
                param_type=ParamType.LR,
                default_val=0.075,
                value_range=[0.0001, 0.5]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=711,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(np.mean(trace['mu']), mu_post, rtol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 42
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_fit_oo[ASVGD-mini]",
        params=[
            Param(
                name="num_samples",
                param_line=708,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="learning-rate",
                param_line=691,
                param_col=58,
                param_type=ParamType.LR,
                default_val=0.07,
                value_range=[0.0001, 0.5]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=711,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(np.mean(trace['mu']), mu_post, rtol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 43
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_fit_oo[ASVGD-full]",
        params=[
            Param(
                name="samples",
                param_line=708,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="lr",
                param_line=687,
                param_col=58,
                param_type=ParamType.LR,
                default_val=0.07,
                value_range=[0.0001, 0.5]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_variational_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=711,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(np.mean(trace['mu']), mu_post, rtol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 44
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_smc.py".format(
            libraries.PROJECT_DIR),
        classname="TestSMCABC",
        testname="test_one_gaussian",
        params=[
            Param(
                name="draws",
                param_line=113,
                param_col=40,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 5000]
            ),
            # Param(
            #     name="epsilon",
            #     param_line=113,
            #     param_col=68,
            #     param_type=ParamType.LR,
            #     default_val=0.1,
            #     value_range=[0.1, 0.9]
            # ),
            Param(
                name="n_steps",
                param_line=113,
                param_col=81,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[10, 2000],
                steps=10
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/test_smc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=115,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="np.testing.assert_almost_equal(self.data.mean(), trace[a].mean(), decimal=1)",
                args=[]
            )
        ]
    ),
    Spec(  # 45
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestMetropolisUniform",
        testname="test_mean",
        params=[
            Param(
                name="n_samples",
                param_line=31,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=50000,
                value_range=[100, 50000]
            ),
            Param(
                name="tune",
                param_line=32,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="burn",
                param_line=33,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=0,
                value_range=[1, 1000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=34,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=28,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="npt.assert_allclose(expected, samples.mean(0), rtol=0.1, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 46
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestNUTSUniform2",
        testname="test_mean",
        params=[
            Param(
                name="n_samples",
                param_line=21,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=22,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="burn",
                param_line=23,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[10, 2000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=24,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=28,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="npt.assert_allclose(expected, samples.mean(0), rtol=0.1, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 47
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestNUTSUniform",
        testname="test_mean",
        params=[
            Param(
                name="n_samples",
                param_line=21,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=22,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="burn",
                param_line=23,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[10, 2000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=24,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=28,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="npt.assert_allclose(expected, samples.mean(0), rtol=0.1, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 48
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestNUTSUniform3",
        testname="test_mean",
        params=[
            Param(
                name="n_samples",
                param_line=21,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=22,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="burn",
                param_line=23,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[10, 2000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=24,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=28,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="npt.assert_allclose(expected, samples.mean(0), rtol=0.1, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 49
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestSliceUniform",
        testname="test_mean",
        params=[
            Param(
                name="n_samples",
                param_line=41,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=42,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="burn",
                param_line=43,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=0,
                value_range=[1, 2000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=44,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=28,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="npt.assert_allclose(expected, samples.mean(0), rtol=0.1, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 50
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestNUTSNormal",
        testname="test_mean",
        params=[
            Param(
                name="n_samples",
                param_line=59,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=60,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="burn",
                param_line=61,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=0,
                value_range=[1, 2000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=62,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=28,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="npt.assert_allclose(expected, samples.mean(0), rtol=0.1, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 51
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestNUTSStudentT",
        testname="test_mean",
        params=[
            Param(
                name="n_samples",
                param_line=78,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=79,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="burn",
                param_line=80,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=0,
                value_range=[1, 2000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=81,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=28,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="npt.assert_allclose(expected, samples.mean(0), rtol=0.1, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(  # 52
        repo="pymc3",
        filename="{0}/projects/pymc3/pymc3/tests/test_posteriors.py".format(
            libraries.PROJECT_DIR),
        classname="TestNUTSLKJCholeskyCov",
        testname="test_kstest",
        params=[
            Param(
                name="n_samples",
                param_line=99,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 10000]
            ),
            Param(
                name="tune",
                param_line=100,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 5000]
            ),
            Param(
                name="burn",
                param_line=101,
                param_col=11,
                param_type=ParamType.ITER,
                default_val=0,
                value_range=[1, 2000],
                steps=10
            ),
            Param(
                name="chains",
                param_line=102,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, 3, 4, 5, 6, None]
            )

        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc3/pymc3/tests/sampler_fixtures.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=54,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert (p > self.alpha)",
                args=[]
            )
        ]
    ),
    Spec(  # 53 travis
        repo="pymc3",
        filename="{0}/tool/travis_builds/pymc3/pymc3/tests/test_variational_inference.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_fit_oo[SVGD-mini]",
        skip=True,
        params=[
            Param(
                name="num_samples",
                param_line=593,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="learning-rate",
                param_line=570,
                param_col=58,
                param_type=ParamType.LR,
                default_val=0.075,
                value_range=[0.0001, 0.5]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/tool/travis_builds/pymc3/pymc3/tests/test_variational_inference.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=596,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(np.mean(trace['mu']), mu_post, rtol=0.05)",
                args=[]
            )
        ]
    ),
    # numpyro tests

    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_mcmc.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_improper_normal",
        params=[
            Param(
                name="num_warmup",
                param_line=138,
                param_col=35,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_samples",
                param_line=138,
                param_col=53,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 1000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_mcmc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(jnp.mean(samples['loc'], 0), true_coef, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_infer_util.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_model_with_mask_false",
        params=[
            Param(
                name="num_warmup",
                param_line=181,
                param_col=35,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_samples",
                param_line=181,
                param_col=52,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_infer_util.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=183,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(mcmc.get_samples()['x'].mean(), 0., atol=0.1)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_svi.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_beta_bernoulli",
        params=[
            Param(
                name="svi_iter",
                param_line=68,
                param_col=29,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_svi.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=70,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(params['alpha_q'] / (params['alpha_q'] + params['beta_q']), 0.8, atol=0.05, rtol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_optimizers.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_optim_multi_params",
        params=[
            Param(
                name="loop_iter",
                param_line=36,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_optimizers.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=39,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert jnp.allclose(param, jnp.zeros(3))",
                args=[]
            )
        ]
    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_infer_util.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_predictive_with_improper",
        params=[
            Param(
                name="num_warmup",
                param_line=116,
                param_col=35,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_samples",
                param_line=116,
                param_col=53,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_infer_util.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=120,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(jnp.mean(obs_pred), true_coef, atol=0.05)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_hmc_util.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_gaussian_subposterior",
        params=[
            Param(
                name="num_samples",
                param_line=402,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),
            Param(
                name="num_draws",
                param_line=403,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=9000,
                value_range=[100, 9000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_hmc_util.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=414,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(jnp.mean(draws, axis=0), mean, atol=0.03)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_distributions.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_beta_binomial_log_prob",
        params=[
            Param(
                name="num_samples",
                param_line=552,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=100000,
                value_range=[100, 100000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_distributions.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=558,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(actual, expected, rtol=0.02)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_distributions.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_gamma_poisson_log_prob",
        params=[
            Param(
                name="num_samples",
                param_line=567,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=300000,
                value_range=[100, 300000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_distributions.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=572,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(actual, expected, rtol=0.05)",
                args=[]
            )
        ]
    ),

    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_mcmc.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_reuse_mcmc_run",
        params=[
            Param(
                name="num_warmup",
                param_line=537,
                param_col=24,
                param_type=ParamType.ITER,
                default_val=300,
                value_range=[100, 300]
            ),
            Param(
                name="num_samples",
                param_line=537,
                param_col=29,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_mcmc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=542,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(mcmc.get_samples()['mu'].mean(), -3., atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_mcmc.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_change_point_x64",
        params=[
            Param(
                name="num_warmup",
                param_line=196,
                param_col=32,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_samples",
                param_line=196,
                param_col=37,
                param_type=ParamType.ITER,
                default_val=3000,
                value_range=[100, 3000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_mcmc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=222,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert mode == 44",
                args=[]
            )
        ]


    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_mcmc.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_logistic_regression_x64",
        params=[
            Param(
                name="num_warmup",
                param_line=77,
                param_col=75,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_samples",
                param_line=77,
                param_col=81,
                param_type=ParamType.ITER,
                default_val=8000,
                value_range=[100, 8000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_mcmc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=97,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(jnp.mean(samples['coefs'], 0), true_coefs, atol=0.22)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_mcmc.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_beta_bernoulli_x64",
        params=[
            Param(
                name="num_warmup",
                param_line=146,
                param_col=75,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_samples",
                param_line=146,
                param_col=80,
                param_type=ParamType.ITER,
                default_val=20000,
                value_range=[100, 20000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_mcmc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=165,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(jnp.mean(samples['p_latent'], 0), true_probs, atol=0.05)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="numpyro",
        filename="{0}/projects/numpyro/test/test_mcmc.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_functional_beta_bernoulli_x64",
        params=[
            Param(
                name="num_warmup",
                param_line=471,
                param_col=32,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_samples",
                param_line=471,
                param_col=37,
                param_type=ParamType.ITER,
                default_val=20000,
                value_range=[100, 20000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/numpyro/test/test_mcmc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=489,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="assert_allclose(jnp.mean(samples['p_latent'], 0), true_probs, atol=0.05)",
                args=[]
            )
        ]


    ),


    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_kissgp_additive_classification.py".format(
            libraries.PROJECT_DIR),
        classname="TestKISSGPAdditiveClassification",
        testname="test_kissgp_classification_error",
        params=[
            Param(
                name="learning-rate",
                param_line=76,
                param_col=58,
                param_type=ParamType.LR,
                default_val=0.15,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="loop_iter",
                param_line=78,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[1, 25],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_kissgp_additive_classification.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=102,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error.squeeze().item(), 0.15)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_svgp_gp_classification.py".format(
            libraries.PROJECT_DIR),
        classname="TestSVGPClassification",
        testname="test_classification_error",
        params=[
            Param(
                name="num_steps",
                param_line=52,
                param_col=61,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[1, 25],
                steps=1
            ),
            Param(
                name="learning-rate",
                param_line=62,
                param_col=105,
                param_type=ParamType.LR,
                default_val=0.1,
                value_range=[1e-5, 1.0]
            ),

            Param(
                name="loop_iter",
                param_line=67,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=400,
                value_range=[10, 400],
                steps=10
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_svgp_gp_classification.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=86,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error.item(), 2e-1)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_svgp_gp_classification.py".format(
            libraries.PROJECT_DIR),
        classname="TestSVGPClassification",
        testname="test_predictive_ll_classification_error",
        params=[
            Param(
                name="num_steps",
                param_line=52,
                param_col=61,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[1, 25],
                steps=1
            ),
            Param(
                name="learning-rate",
                param_line=62,
                param_col=105,
                param_type=ParamType.LR,
                default_val=0.1,
                value_range=[1.0e-5, 10]
            ),

            Param(
                name="loop_iter",
                param_line=67,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=400,
                value_range=[10, 400],
                steps=10
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_svgp_gp_classification.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=86,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error.item(), 2e-1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_batch_svgp_gp_regression.py".format(
            libraries.PROJECT_DIR),
        classname="TestSVGPRegression",
        testname="test_regression_error",
        params=[
            Param(
                name="num_steps",
                param_line=68,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[1, 25],
                steps=1
            ),
            Param(
                name="loop_iter",
                param_line=76,
                param_col=23,
                param_type=ParamType.ITER,
                default_val=180,
                value_range=[10, 180],
                steps=10
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_batch_svgp_gp_regression.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=98,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error2.item(), 1e-1)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_batch_svgp_gp_regression.py".format(
            libraries.PROJECT_DIR),
        classname="TestSVGPRegression",
        testname="test_regression_error_shared_inducing_locations",
        params=[
            Param(
                name="num_steps",
                param_line=103,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[1, 25],
                steps=1
            ),
            Param(
                name="loop_iter",
                param_line=111,
                param_col=23,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_batch_svgp_gp_regression.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=133,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error2.item(), 1e-1)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_kissgp_multiplicative_regression.py".format(
            libraries.PROJECT_DIR),
        classname="TestKISSGPMultiplicativeRegression",
        testname="test_kissgp_gp_mean_abs_error",
        params=[
            Param(
                name="learning-rate",
                param_line=78,
                param_col=95,
                param_type=ParamType.LR,
                default_val=0.2,
                value_range=[1.0e-5, 1.0]
            ),
            Param(
                name="loop_iter",
                param_line=80,
                param_col=23,
                param_type=ParamType.ITER,
                default_val=15,
                value_range=[1, 15],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_kissgp_multiplicative_regression.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=102,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error.squeeze().item(), 0.15)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_spectral_mixture_gp_regression.py".format(
            libraries.PROJECT_DIR),
        classname="TestSpectralMixtureGPRegression",
        testname="test_spectral_mixture_gp_mean_abs_error",
        params=[
            #            Param(
            #                name="param1",
            #                param_line=75,
            #                param_col=62,
            #                param_type=ParamType.LR,
            #                default_val=0.1,
            #                value_range=[0.0001, 1.0]
            #            ),
            Param(
                name="loop_iter",
                param_line=81,
                param_col=23,
                param_type=ParamType.ITER,
                default_val=300,
                value_range=[10, 300],
                steps=10
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_spectral_mixture_gp_regression.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=103,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error.squeeze().item(), 0.2)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_unwhitened_svgp_regression.py".format(
            libraries.PROJECT_DIR),
        classname="TestSVGPRegression",
        testname="test_regression_error",
        params=[
            Param(
                name="num_steps",
                param_line=53,
                param_col=57,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[1, 25],
                steps=1
            ),
            Param(
                name="loop_iter",
                param_line=66,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200],
                steps=10
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_unwhitened_svgp_regression.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=85,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error.item(), 1e-1)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="gpytorch",
        filename="{0}/projects/gpytorch/test/examples/test_kissgp_gp_classification.py".format(
            libraries.PROJECT_DIR),
        classname="TestKISSGPClassification",
        testname="test_kissgp_classification_error",
        params=[
            Param(
                name="loop_iter",
                param_line=69,
                param_col=23,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200],
                steps=10
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/gpytorch/test/examples/test_kissgp_gp_classification.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=90,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(mean_abs_error.squeeze().item(), 1e-5)",
                args=[]
            )
        ]


    ),


    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_mdn.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_mdn_with_snpe",
        params=[
            Param(
                name="num_samples",
                param_line=32,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=52,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="training_batch_size",
                param_line=52,
                param_col=74,
                param_type=ParamType.ITER,
                default_val=50,
                value_range=[10, 50]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_mdn.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_mdn_with_snle",
        params=[
            Param(
                name="num_samples",
                param_line=32,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=52,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="training_batch_size",
                param_line=52,
                param_col=74,
                param_type=ParamType.ITER,
                default_val=50,
                value_range=[10, 50]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snle_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snl_on_linearGaussian[uniform-1]",
        params=[
            Param(
                name="num_samples",
                param_line=120,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=148,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snle_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snl_on_linearGaussian[uniform-2]",
        params=[
            Param(
                name="num_samples",
                param_line=120,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=148,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snle_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snl_on_linearGaussian[gaussian-1]",
        params=[
            Param(
                name="num_samples",
                param_line=120,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=148,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snle_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snl_on_linearGaussian[gaussian-2]",
        params=[
            Param(
                name="num_samples",
                param_line=120,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=148,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snle_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_multi_round_snl_on_linearGaussian",
        params=[
            Param(
                name="num_samples",
                param_line=175,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=198,
                param_col=71,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snpe_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snpe_on_linearGaussian[2-gaussian]",
        params=[
            Param(
                name="num_samples",
                param_line=42,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=74,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snpe_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snpe_on_linearGaussian[2-uniform]",
        params=[
            Param(
                name="num_samples",
                param_line=42,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=74,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snpe_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snpe_on_linearGaussian[1-gaussian]",
        params=[
            Param(
                name="num_samples",
                param_line=42,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=74,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snpe_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snpe_on_linearGaussian_different_dims",
        params=[
            Param(
                name="num_samples",
                param_line=135,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=167,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snpe_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_multi_round_snpe_on_linearGaussian",
        params=[
            Param(
                name="num_samples",
                param_line=197,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=221,
                param_col=70,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snre_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_sre_on_linearGaussian_different_dims",
        params=[
            Param(
                name="num_samples",
                param_line=70,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=103,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snre_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_sre_on_linearGaussian",
        params=[
            Param(
                name="num_samples",
                param_line=132,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=168,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/multiprocessing_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_benchmarking_sp[1]",
        params=[
            Param(
                name="num_simulations",
                param_line=30,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/multiprocessing_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=55,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert toc_joblib <= toc_sp * 1.1",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/multiprocessing_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_benchmarking_sp[10]",
        params=[
            Param(
                name="num_simulations",
                param_line=30,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/multiprocessing_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=55,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert toc_joblib <= toc_sp * 1.1",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/multiprocessing_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_benchmarking_sp[100]",
        params=[
            Param(
                name="num_simulations",
                param_line=30,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/multiprocessing_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=55,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert toc_joblib <= toc_sp * 1.1",
                args=[]
            )
        ]


    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/inference_with_NaN_simulator_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_inference_with_nan_simulator[SNPE_C-True-0.05]",
        params=[
            Param(
                name="num_samples",
                param_line=55,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations",
                param_line=56,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/inference_with_NaN_simulator_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_inference_with_nan_simulator[SNLE_A-True-0.05]",
        params=[
            Param(
                name="num_samples",
                param_line=55,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations",
                param_line=56,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/inference_with_NaN_simulator_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_inference_with_nan_simulator[SNRE_B-True-0.05]",
        params=[
            Param(
                name="num_samples",
                param_line=55,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="num_simulations",
                param_line=56,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=2000,
                value_range=[100, 2000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="sbi",
        filename="{0}/projects/sbi/tests/linearGaussian_snle_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_c2st_snl_on_linearGaussian_different_dims",
        params=[
            Param(
                name="num_samples",
                param_line=69,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="num_simulations_per_round",
                param_line=100,
                param_col=62,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/sbi/tests/test_utils.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(score, val, rtol=0, atol=0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
            libraries.PROJECT_DIR),
        classname="TestGaussianProcessRegressorPredict",
        testname="test_predict_returns_predictions",
        params=[
            Param(
                name="n",
                param_line=91,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=93,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(self.y_test.shape, preds.shape)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
            libraries.PROJECT_DIR),
        classname="TestGaussianProcessRegressorPredict",
        testname="test_predict_returns_mean_predictions_and_std",
        skip=True, # cant run in parallel
        params=[
            Param(
                name="n",
                param_line=98,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=100,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(self.y_test.shape, stds.shape)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
            libraries.PROJECT_DIR),
        classname="TestGaussianProcessRegressorScore",
        testname="test_score_matches_sklearn_performance",
        skip=True,
        params=[
            Param(
                name="n",
                param_line=118,
                param_col=47,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=121,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="npt.assert_almost_equal(sk_gpr_score, advi_gpr_score, 1)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
            libraries.PROJECT_DIR),
        classname="TestStudentsTProcessRegressorFit",
        testname="test_advi_fit_returns_correct_model",
        skip=True,
        params=[
            Param(
                name="n",
                param_line=190,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=192,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(self.num_pred, self.advi_stpr.num_pred)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
            libraries.PROJECT_DIR),
        classname="TestStudentsTProcessRegressorScore",
        testname="test_score_matches_sklearn_performance",
        skip=True,
        params=[
            Param(
                name="n",
                param_line=238,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=241,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="npt.assert_almost_equal(sk_gpr_score, advi_stpr_score, 0)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
            libraries.PROJECT_DIR),
        classname="TestSparseGaussianProcessRegressorPredict",
        testname="test_predict_returns_predictions",
        params=[
            Param(
                name="n",
                param_line=331,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=333,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(self.y_test.shape, preds.shape)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
            libraries.PROJECT_DIR),
        classname="TestSparseGaussianProcessRegressorPredict",
        testname="test_predict_returns_predictions",
        params=[
            Param(
                name="n",
                param_line=338,
                param_col=48,
                param_type=ParamType.ITER,
                default_val=25000,
                value_range=[100, 25000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=341,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(self.y_test.shape, preds.shape)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
            libraries.PROJECT_DIR),
        classname="TestHierarchicalLogisticRegressionFit",
        testname="test_advi_fit_returns_correct_model",
        skip=True, # cant run in parallel
        params=[
            Param(
                name="n",
                param_line=76,
                param_col=67,
                param_type=ParamType.ITER,
                default_val=50000,
                value_range=[100, 50000]
            ),
            Param(
                name="minibatch_size",
                param_line=76,
                param_col=41,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/gaussian_process/tests/test_gpr.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=89,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(np.sign(self.alphas),np.sign(self.advi_hlr.trace['alpha'].mean(axis=0)))",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
            libraries.PROJECT_DIR),
        classname="TestHierarchicalLogisticRegressionPredictProba",
        testname="test_predict_proba_returns_probabilities",
        params=[
            Param(
                name="n",
                param_line=105,
                param_col=67,
                param_type=ParamType.ITER,
                default_val=50000,
                value_range=[100, 50000]
            ),
            Param(
                name="minibatch_size",
                param_line=105,
                param_col=41,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=107,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(probs.shape, self.y_test.shape)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
            libraries.PROJECT_DIR),
        classname="TestHierarchicalLogisticRegressionPredictProba",
        testname="test_predict_proba_returns_probabilities_and_std",
        params=[
            Param(
                name="n",
                param_line=112,
                param_col=67,
                param_type=ParamType.ITER,
                default_val=50000,
                value_range=[100, 50000]
            ),
            Param(
                name="minibatch_size",
                param_line=112,
                param_col=41,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=115,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(probs.shape, self.y_test.shape)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
            libraries.PROJECT_DIR),
        classname="TestHierarchicalLogisticRegressionPredict",
        testname="test_predict_returns_predictions",
        params=[
            Param(
                name="n",
                param_line=130,
                param_col=67,
                param_type=ParamType.ITER,
                default_val=50000,
                value_range=[100, 50000]
            ),
            Param(
                name="minibatch_size",
                param_line=130,
                param_col=41,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=132,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="npt.assert_equal(preds.shape, self.y_test.shape)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
            libraries.PROJECT_DIR),
        classname="TestHierarchicalLogisticRegressionScore",
        testname="test_score_scores",
        params=[
            Param(
                name="n",
                param_line=141,
                param_col=67,
                param_type=ParamType.ITER,
                default_val=50000,
                value_range=[100, 50000]
            ),
            Param(
                name="minibatch_size",
                param_line=141,
                param_col=41,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=144,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ARRAY_LESS,
                assert_string="npt.assert_array_less(naive_score, score)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pymc-learn",
        filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
            libraries.PROJECT_DIR),
        classname="TestHierarchicalLogisticRegressionSaveandLoad",
        testname="test_save_and_load_work_correctly",
        params=[
            Param(
                name="n",
                param_line=153,
                param_col=67,
                param_type=ParamType.ITER,
                default_val=50000,
                value_range=[100, 50000]
            ),
            Param(
                name="minibatch_size",
                param_line=153,
                param_col=41,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[10, 500]
            )
        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pymc-learn/pmlearn/linear_model/tests/test_logistic.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=170,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="npt.assert_almost_equal(probs2, probs1, decimal=1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pyGPGO",
        filename="{0}/projects/pyGPGO/tests/test_covfunc.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_psd_covfunc",
        skip=True, # complex func
        params=[
            Param(
                name="loop_iter",
                param_line=43,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[1, 100],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyGPGO/tests/test_covfunc.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=46,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ARRAY_LESS,
                assert_string="np.testing.assert_array_less(-eigvals, 0)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pyGPGO",
        filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_GPGO",
        params=[
            Param(
                name="max_iter",
                param_line=22,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=24,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(res['x'], 0.7, atol=0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pyGPGO",
        filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_GPGO_mcmc",
        params=[
            Param(
                name="max_iter",
                param_line=35,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=37,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(res['x'], 0.7, atol=0.1)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="pyGPGO",
        filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_GPGO_sk",
        params=[
            Param(
                name="max_iter",
                param_line=47,
                param_col=22,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/pyGPGO/tests/test_GPGO.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=49,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(res['x'], 0.75, atol=0.05)",
                args=[]
            )
        ]


    ),
    # multiple asserts for this test
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFBertModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_bert.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=144,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(result[\"pooled_output\"].shape), [self.batch_size, self.hidden_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFCTRLModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_bert.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFMobileBertModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_mobilebert.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFXLNetModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_xlnet.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFDistilBertModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_distilbert.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFT5ModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_t5.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFGPT2ModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_gpt2.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFXLMModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_xlm.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFRobertaModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_roberta.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFElectraModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_electra.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFAlbertModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_albert.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFTransfoXLModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_transfo_xl.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="transformers",
    #        filename="{0}/projects/transformers/tests/test_modeling_tf_common.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="TFModelTesterMixin",
    #        testname="test_compile_tf_model",
    #        params=[
    #            Param(
    #                name="learning_rate",
    #                param_line=293,
    #                param_col=59,
    #                param_type=ParamType.LR,
    #                default_val=3e-5,
    #                value_range=[3e-5, 1.0]
    #            ),
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname="test_compile_tf_model",
    #                          classname="TFOpenAIGPTModelTest",
    #                          filename="{0}/projects/transformers/tests/test_modeling_tf_openai_gpt.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=157,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT_LIST_EQUAL,
    #                assert_string="self.parent.assertListEqual(list(prediction_scores.numpy().shape), [self.batch_size, self.seq_length, self.vocab_size])",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),


    #    Spec(
    #        repo="fastai",
    #        filename="{0}/projects/fastai/tests/test_text_languagemodelpreloader.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="none",
    #        testname="test_backwards_minibatch",
    #        params=[
    #            Param(
    #                name="nbTests",
    #                param_line=70,
    #                param_col=100,
    #                param_type=ParamType.ITER,
    #                default_val=1000,
    #                value_range=[100, 1000]
    #            ),
    #
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname=None,
    #                          classname=None,
    #                          filename="{0}/projects/fastai/tests/test_text_languagemodelpreloader.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=52,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT,
    #                assert_string="assert np.all(batches[ix-1,-1]+diff == batches[ix,0]), f"last token i row-1 {batches[ix-1,-1]}+{diff} must be equal to first element in row:{batches[ix,0]}"",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    #    Spec(
    #        repo="fastai",
    #        filename="{0}/projects/fastai/tests/test_text_languagemodelpreloader.py".format(
    #            libraries.PROJECT_DIR),
    #        classname="none",
    #        testname="test_forward_minibatch",
    #        params=[
    #            Param(
    #                name="nbTests",
    #                param_line=71,
    #                param_col=101,
    #                param_type=ParamType.ITER,
    #                default_val=1000,
    #                value_range=[100, 1000]
    #            ),
    #
    #
    #        ],
    #        assertions=[
    #
    #            AssertSpec(
    #                test=Test(testname=None,
    #                          classname=None,
    #                          filename="{0}/projects/fastai/tests/test_text_languagemodelpreloader.py".format(
    #                              libraries.PROJECT_DIR)
    #                          ),
    #                line=52,
    #                col_offset=-1,
    #                assert_type=AssertType.ASSERT,
    #                assert_string="assert np.all(batches[ix-1,-1]+diff == batches[ix,0]), f"last token i row-1 {batches[ix-1,-1]}+{diff} must be equal to first element in row:{batches[ix,0]}"",
    #                args=[]
    #            )
    #        ]
    #
    #
    #    ),
    Spec(
        repo="flair",
        filename="{0}/projects/flair/tests/test_text_classifier.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_train_load_use_classifier",
        skip=True,
        params=[
            Param(
                name="max_epochs",
                param_line=48,
                param_col=48,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, None]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/flair/tests/test_text_classifier.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=56,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert 0.0 <= label.score <= 1.0",
                args=[]
            )
        ]


    ),
    Spec(
        repo="flair",
        filename="{0}/projects/flair/tests/test_text_classifier.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_train_load_use_classifier_with_sampler",
        skip=True,
        params=[
            Param(
                name="max_epochs",
                param_line=84,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, None]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/flair/tests/test_text_classifier.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=94,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert 0.0 <= label.score <= 1.0",
                args=[]
            )
        ]


    ),
    Spec(
        repo="flair",
        filename="{0}/projects/flair/tests/test_text_classifier.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_train_load_use_classifier_multi_label",
skip=True,
        params=[
            Param(
                name="max_epochs",
                param_line=161,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[1, 100],
                steps=1
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/flair/tests/test_text_classifier.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=185,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert 0.0 <= label.score <= 1.0",
                args=[]
            )
        ]


    ),
    Spec(
        repo="flair",
        filename="{0}/projects/flair/tests/test_language_model.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_train_language_model",
skip=True,
        params=[
            Param(
                name="max_epochs",
                param_line=32,
                param_col=78,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, None]
            ),
            Param(
                name="mini_batch_size",
                param_line=32,
                param_col=63,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/flair/tests/test_language_model.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=44,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert len(text) >= 100",
                args=[]
            )
        ]


    ),
    Spec(
        repo="fastai",
        filename="{0}/projects/fastai/tests/test_train.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_fit_one_cycle",
        skip=True,  # < 1 second
        params=[
            Param(
                name="lr",
                param_line=40,
                param_col=23,
                param_type=ParamType.LR,
                default_val=3e-3,
                value_range=[1e-5, 1]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/fastai/tests/test_train.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=52,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert idx_lr == idx_mom",
                args=[]
            )
        ]


    ),
    Spec(
        repo="fastai",
        filename="{0}/projects/fastai/tests/test_train.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_fit",
        skip=True,  # < 1 second
        params=[
            Param(
                name="lr",
                param_line=31,
                param_col=39,
                param_type=ParamType.LR,
                default_val=3e-3,
                value_range=[1e-5, 1]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/fastai/tests/test_train.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=33,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert set(learn.recorder.lrs) == {learning_rate}",
                args=[]
            )
        ]


    ),
    Spec(
        repo="fastai",
        filename="{0}/projects/fastai/tests/test_train.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_lr_find",
        skip=True,
        params=[
            Param(
                name="loop_iter",
                param_line=19,
                param_col=66,
                param_type=ParamType.ITER,
                default_val=90,
                value_range=[10, 90]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/fastai/tests/test_train.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=23,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert learn.recorder.lrs[-1] < learn.recorder.opt.lr",
                args=[]
            )
        ]

    ),
    Spec(
        repo="horovod",
        filename="{0}/projects/horovod/test/test_keras.py".format(
            libraries.PROJECT_DIR),
        classname="KerasTests",
        testname="test_load_model",
        params=[
            Param(
                name="lr",
                param_line=68,
                param_col=46,
                param_type=ParamType.LR,
                default_val=0.0001,
                value_range=[0.0001, 1]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/horovod/test/test_keras.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=92,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(K.get_value(opt.lr), K.get_value(new_opt.lr))",
                args=[]
            )
        ]


    ),
    Spec(
        repo="horovod",
        filename="{0}/projects/horovod/test/test_spark_torch.py".format(
            libraries.PROJECT_DIR),
        classname="SparkTorchTests",
        testname="test_fit_model",
skip=True,
        params=[
            Param(
                name="lr",
                param_line=76,
                param_col=59,
                param_type=ParamType.LR,
                default_val=0.1,
                value_range=[0.1, 1.0]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/horovod/test/test_keras.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=102,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert pred.dtype == torch.float32",
                args=[]
            )
        ]


    ),
    Spec(
        repo="horovod",
        filename="{0}/projects/horovod/test/test_spark_torch.py".format(
            libraries.PROJECT_DIR),
        classname="SparkTorchTests",
        testname="test_torch_direct_parquet_train",
skip=True,
        params=[
            Param(
                name="lr",
                param_line=351,
                param_col=71,
                param_type=ParamType.LR,
                default_val=0.1,
                value_range=[0.1, 1.0]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/horovod/test/test_spark_torch.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=371,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert predictions.count() == df.count()",
                args=[]
            )
        ]


    ),

    Spec(
        repo="allennlp",
        filename="{0}/projects/allennlp/tests/training/trainer_test.py".format(
            libraries.PROJECT_DIR),
        classname="TestTrainer",
        testname="test_trainer_respects_keep_serialized_model_every_num_seconds",
        skip=True,
        params=[
            Param(
                name="num_epochs",
                param_line=680,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=6,
                value_range=[1, 2, 3, 4, 5, 6, None]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/allennlp/tests/training/trainer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=695,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert sorted(epochs) == [1, 3, 4, 5]",
                args=[]
            )
        ]


    ),
    Spec(
        repo="allennlp",
        filename="{0}/projects/allennlp/tests/training/trainer_test.py".format(
            libraries.PROJECT_DIR),
        classname="TestTrainer",
        testname="test_trainer_can_run_and_resume_with_momentum_scheduler",
        skip=True,
        params=[
            Param(
                name="num_epochs",
                param_line=536,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=6,
                value_range=[1, 2, 3, 4, 5, 6, None]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/allennlp/tests/training/trainer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=541,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert new_trainer._momentum_scheduler.last_epoch == 3",
                args=[]
            )
        ]


    ),
    Spec(
        repo="allennlp",
        filename="{0}/projects/allennlp/tests/training/trainer_test.py".format(
            libraries.PROJECT_DIR),
        classname="TestTrainer",
        testname="test_trainer_respects_num_serialized_models_to_keep",
        skip=True,
        params=[
            Param(
                name="num_epochs",
                param_line=622,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=5,
                value_range=[1, 2, 3, 4, 5, None]
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/allennlp/tests/training/trainer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=634,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert sorted(epochs) == [2, 3, 4]",
                args=[]
            )
        ]


    ),
    Spec(
        repo="allennlp",
        filename="{0}/projects/allennlp/tests/training/checkpointer_test.py".format(
            libraries.PROJECT_DIR),
        classname="TestCheckpointer",
        testname="test_with_time",
        skip=True,
        params=[
            Param(
                name="num_epochs",
                param_line=84,
                param_col=21,
                param_type=ParamType.ITER,
                default_val=30,
                value_range=[1, 30],
                steps=1
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/allennlp/tests/training/checkpointer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=102,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert models == training == target",
                args=[]
            )
        ]


    ),
    Spec(
        repo="allennlp",
        filename="{0}/projects/allennlp/tests/training/checkpointer_test.py".format(
            libraries.PROJECT_DIR),
        classname="TestCheckpointer",
        testname="test_default",
        skip=True,
        params=[
            Param(
                name="num_epochs",
                param_line=50,
                param_col=21,
                param_type=ParamType.ITER,
                default_val=30,
                value_range=[1, 30],
                steps=1
            ),


        ],
        assertions=[

            AssertSpec(
                test=Test(testname=None,
                          classname=None,
                          filename="{0}/projects/allennlp/tests/training/checkpointer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=62,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert models == training == target",
                args=[]
            )
        ]


    ),
    Spec(
        repo="fairseq",
        filename="{0}/projects/fairseq/tests/test_multi_corpus_sampled_dataset.py".format(
            libraries.PROJECT_DIR),
        classname="TestMultiCorpusSampledDataset",
        testname="test_multi_corpus_sampled_dataset_uniform_sample",
        params=[
            Param(
                name="num_epochs",
                param_line=47,
                param_col=20,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/fairseq/tests/test_multi_corpus_sampled_dataset.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=69,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(abs(sample_from_first_ds_percentage - expected_sample_from_first_ds_percentage),0.01,)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="fairseq",
        filename="{0}/projects/fairseq/tests/test_multi_corpus_sampled_dataset.py".format(
            libraries.PROJECT_DIR),
        classname="TestMultiCorpusSampledDataset",
        testname="test_multi_corpus_sampled_dataset_weighted_sample",
        params=[
            Param(
                name="num_epochs",
                param_line=47,
                param_col=20,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/fairseq/tests/test_multi_corpus_sampled_dataset.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=69,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(abs(sample_from_first_ds_percentage - expected_sample_from_first_ds_percentage),0.01,)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="autokeras",
        filename="{0}/projects/autokeras/tests/integration_tests/task_api_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_structured_data_from_numpy_regressor",
        params=[
            Param(
                name="num_epochs",
                param_line=57,
                param_col=37,
                param_type=ParamType.CHAINS,
                default_val=11,
                value_range=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            )


        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/autokeras/tests/integration_tests/task_api_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=59,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert clf.predict(x_test).shape == (len(y_test), 1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="autokeras",
        filename="{0}/projects/autokeras/tests/integration_tests/task_api_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_structured_data_from_numpy_classifier",
        params=[
            Param(
                name="num_epochs",
                param_line=72,
                param_col=37,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, None]
            )


        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/autokeras/tests/integration_tests/task_api_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=74,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert clf.predict(x_test).shape == (len(y_test), 3)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_transformers.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_repeater",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=29,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=26,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128, 256]
            )


        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_transformers.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=50,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(test['hits@1'], 0.90)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_transformers.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerGenerator",
        testname="test_xlm",
        params=[
            Param(
                name="learning_rate",
                param_line=539,
                param_col=29,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="epoch",
                param_line=541,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=20,
                value_range=[1, 20],
                steps=1
            ),
            Param(
                name="batchsize",
                param_line=540,
                param_col=26,
                param_type=ParamType.CHAINS,
                default_val=32,
                value_range=[2, 8, 16, 32, 64, 128, 256]
            )


        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_transformers.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=557,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESSEQUAL,
                assert_string="self.assertLessEqual(test['ppl'], 1.30)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_transformers.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerGenerator",
        testname="test_beamsearch",
        params=[
            Param(
                name="learning_rate",
                param_line=289,
                param_col=29,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="epoch",
                param_line=291,
                param_col=27,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            ),
            Param(
                name="batchsize",
                param_line=290,
                param_col=26,
                param_type=ParamType.CHAINS,
                default_val=32,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )


        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_transformers.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=305,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(test['bleu-4'], 0.90)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_transformers.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_alt_reduction",
        params=[
            Param(
                name="learning_rate",
                param_line=226,
                param_col=29,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="batchsize",
                param_line=227,
                param_col=26,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_transformers.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=244,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(test['hits@1'], 0.90)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_seq2seq.py".format(
            libraries.PROJECT_DIR),
        classname="TestHogwildSeq2seq",
        testname="test_generation_multi",
        params=[
            Param(
                name="learning_rate",
                param_line=12,
                param_col=5,
                param_type=ParamType.LR,
                default_val=1,
                value_range=[1e-3, 10]
            ),
            Param(
                name="epochs",
                param_line=11,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            ),
            Param(
                name="batch_size",
                param_line=10,
                param_col=13,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 128, 256]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_seq2seq.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=127,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(test['ppl'], 1.2)",
                args=[]
            )
        ]


    ),
    # replacing _AbstractTRATest
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_train_inline",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=54,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_train_batch",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=64,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_train_fixed",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=75,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_train_batch_all",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=85,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_eval_inline",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=95,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_eval_batch",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=105,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_eval_fixed",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=136,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@100'], 0.1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestTransformerRanker",
        testname="test_eval_vocab",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=148,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="self.assertEqual(valid['hits@100'], 0)",
                args=[]
            )
        ]


    ),
    # other instances of _AbstractClass
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_train_inline",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=54,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_train_batch",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=64,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_train_fixed",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=75,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_train_batch_all",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=85,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_eval_inline",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=95,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_eval_batch",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=105,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_eval_fixed",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=136,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@100'], 0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestMemNN",
        testname="test_eval_vocab",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=148,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="self.assertEqual(valid['hits@100'], 0)",
                args=[]
            )
        ]
    ),
    # another instance of #_abstractclass
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_train_inline",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=54,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_train_batch",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=64,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_train_fixed",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=75,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_train_batch_all",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=85,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_eval_inline",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=95,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_eval_batch",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=105,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@1'], threshold)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_eval_fixed",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=136,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(valid['hits@100'], 0.1)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="parlai",
        filename="{0}/projects/parlai/tests/test_tra.py".format(
            libraries.PROJECT_DIR),
        classname="TestPolyRanker",
        testname="test_eval_vocab",
        params=[
            Param(
                name="learning_rate",
                param_line=35,
                param_col=25,
                param_type=ParamType.LR,
                default_val=7e-3,
                value_range=[1e-5, 1]
            ),
            Param(
                name="num_epochs",
                param_line=38,
                param_col=23,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4, None]
            ),
            Param(
                name="batchsize",
                param_line=36,
                param_col=22,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 8, 16, 32, 64, 128]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/parlai/tests/test_tra.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=148,
                col_offset=-1,
                assert_type=AssertType.ASSERT_EQUAL,
                assert_string="self.assertEqual(valid['hits@100'], 0)",
                args=[]
            )
        ]

    ),
    Spec(
        repo="cleverhans",
        filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
            libraries.PROJECT_DIR),
        classname="TestSPSA",
        testname="test_adv_example_success_rate_l2",
        params=[
            Param(
                name="nb_iter",
                param_line=365,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=50,
                value_range=[10, 50]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=47,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(adv_acc, .5)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="cleverhans",
        filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
            libraries.PROJECT_DIR),
        classname="TestSPSA",
        testname="test_targeted_adv_example_success_rate_l2",
        params=[
            Param(
                name="nb_iter",
                param_line=365,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=50,
                value_range=[10, 50]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=59,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATER,
                assert_string="self.assertGreater(adv_success, .7)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="cleverhans",
        filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
            libraries.PROJECT_DIR),
        classname="TestSPSA",
        testname="test_targeted_adv_example_success_rate_linf",
        params=[
            Param(
                name="nb_iter",
                param_line=365,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=50,
                value_range=[10, 50]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=59,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATER,
                assert_string="self.assertGreater(adv_success, .7)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="cleverhans",
        filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
            libraries.PROJECT_DIR),
        classname="TestSPSA",
        testname="test_adv_example_success_rate_linf",
        params=[
            Param(
                name="nb_iter",
                param_line=365,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=50,
                value_range=[10, 50]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=47,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(adv_acc, .5)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="cleverhans",
        filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
            libraries.PROJECT_DIR),
        classname="TestSPSA",
        testname="test_attack_strength",
        params=[
            Param(
                name="nb_iter",
                param_line=422,
                param_col=42,
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
                          filename="{0}/projects/cleverhans/cleverhans/future/torch/tests/test_attacks.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=429,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(adv_acc, .1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="magenta",
        filename="{0}/projects/magenta/magenta/models/rl_tuner/rl_tuner_test.py".format(
            libraries.PROJECT_DIR),
        classname="RLTunerTest",
        testname="testTraining",
        skip=True,  # assertion limits min iterations to 30
        params=[
            Param(
                name="num_steps",
                param_line=100,
                param_col=24,
                param_type=ParamType.ITER,
                default_val=31,
                value_range=[1, 31],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/magenta/magenta/models/rl_tuner/rl_tuner_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=113,
                col_offset=-1,
                assert_type=AssertType.ASSERTTRUE,
                assert_string="self.assertTrue(len(rlt.eval_avg_reward) >= 1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="magenta",
        filename="{0}/projects/magenta/magenta/contrib/rnn_test.py".format(
            libraries.PROJECT_DIR),
        classname="StackBidirectionalRNNTest",
        testname="testBidirectionalRNN",
skip=True,
        params=[
            Param(
                name="input_size",
                param_line=272,
                param_col=17,
                param_type=ParamType.CHAINS,
                default_val=5,
                value_range=[1, 2, 3, 4, 5, None]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/magenta/magenta/contrib/rnn_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=441,
                col_offset=-1,
                assert_type=AssertType.ASSERTALLEQUAL,
                assert_string="self.assertAllEqual(st_5_bw[0], st_5p_bw[0])",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_ldamodel.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaModel",
        testname="testTransform",
        skip=True,
        params=[
            Param(
                name="loop_iter",
                param_line=50,
                param_col=23,
                param_type=ParamType.ITER,
                default_val=25,
                value_range=[1, 25],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_ldamodel.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=68,
                col_offset=-1,
                assert_type=AssertType.ASSERTTRUE,
                assert_string="self.assertTrue(passed)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaWrapper",
        testname="testSetGetParams",
        params=[
            Param(
                name="num_passes",
                param_line=307,
                param_col=53,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[1, 100],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=402,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(getattr(self.model.gensim_model, 'decay'), 0.7)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaWrapper",
        testname="testTransform",
        params=[
            Param(
                name="num_passes",
                param_line=307,
                param_col=53,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[1, 100],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=323,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(matrix.shape[1], self.model.num_topics)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaWrapper",
        testname="testPipeline",
        params=[
            Param(
                name="num_passes",
                param_line=369,
                param_col=52,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=382,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATEREQUAL,
                assert_string="self.assertGreaterEqual(score, 0.40)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaWrapper",
        testname="testPersistence",
        skip=True,
        params=[
            Param(
                name="num_passes",
                param_line=307,
                param_col=53,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[1, 100],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=420,
                col_offset=-1,
                assert_type=AssertType.ASSERTTRUE,
                assert_string="self.assertTrue(passed)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaSeqWrapper",
        testname="testTransform",
        params=[
            Param(
                name="max_iter",
                param_line=526,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=541,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(transformed_vecs.shape[1], self.model.num_topics)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaSeqWrapper",
        testname="testPipeline",
        params=[
            Param(
                name="max_iter",
                param_line=556,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=562,
                col_offset=-1,
                assert_type=AssertType.ASSERTGREATER,
                assert_string="self.assertGreater(score, 0.50)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaSeqWrapper",
        testname="testSetGetParams",
        params=[
            Param(
                name="max_iter",
                param_line=526,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=571,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(getattr(self.model.gensim_model, 'num_topics'), 3)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaSeqWrapper",
        testname="testPersistence",
        # skipping due to no interesting asserts , e..g assertTrue(passed)
        skip=True,
        params=[
            Param(
                name="max_iter",
                param_line=526,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_sklearn_api.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=587,
                col_offset=-1,
                assert_type=AssertType.ASSERTTRUE,
                assert_string="self.assertTrue(passed)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_ldaseqmodel.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaSeq",
        testname="testTopicWord",
        params=[
            Param(
                name="max_iter",
                param_line=208,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_ldaseqmodel.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=217,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="self.assertAlmostEqual(topics[0][0][1], expected_topic_word[0][1], places=2)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_ldaseqmodel.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaSeq",
        testname="testDocTopic",
        params=[
            Param(
                name="max_iter",
                param_line=208,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_ldaseqmodel.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=223,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALMOST_EQUAL,
                assert_string="self.assertAlmostEqual(doc_topic[0], expected_doc_topic, places=2)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_ldaseqmodel.py".format(
            libraries.PROJECT_DIR),
        classname="TestLdaSeq",
        testname="testDtypeBackwardCompatibility",
        params=[
            Param(
                name="max_iter",
                param_line=208,
                param_col=45,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_ldaseqmodel.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=238,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(expected_topics, topics, rtol=1e-05, atol=1e-08)",
                #assert_string="self.assertTrue(np.allclose(expected_topics, topics))",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_word2vec.py".format(
            libraries.PROJECT_DIR),
        classname="TestWord2VecModel",
        testname="testParallel",
        params=[
            Param(
                name="num_iterations",
                param_line=772,
                param_col=49,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_word2vec.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=782,
                col_offset=-1,
                assert_type=AssertType.ASSERTLESS,
                assert_string="self.assertLess(neighbor_rank, 20)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_doc2vec.py".format(
            libraries.PROJECT_DIR),
        classname="TestDoc2VecModel",
        testname="test_training",
        skip=True,  # pickle issue
        # borntobeflaky/tool/scripts/azure/results/run_16-08-20_17_pytorch/logs/optim_1597697903_gensim/run_1597699717/assert_7259425_20/output_0
        params=[
            Param(
                name="epochs",
                param_line=440,
                param_col=69,
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
                line=662,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(len(model.dv.index_to_key), len(model2.dv.index_to_key))",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_doc2vec.py".format(
            libraries.PROJECT_DIR),
        classname="TestDoc2VecModel",
        testname="test_parallel",
        skip=True,  # pickleError when run  in parallel
        # (phoenix) borntobeflaky/tool/scripts/azure/results/run_16-08-20_17_pytorch/logs/optim_1597697903_gensim/run_1597699869/assert_78889776_100/output_0
        params=[
            Param(
                name="num_iterations",
                param_line=610,
                param_col=53,
                param_type=ParamType.ITER,
                default_val=6000,
                value_range=[100, 6000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/gensim/gensim/test/test_doc2vec.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=428,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(model.dv.doesnt_match([fire1, alt1, fire2]), alt1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="gensim",
        filename="{0}/projects/gensim/gensim/test/test_doc2vec.py".format(
            libraries.PROJECT_DIR),
        classname="TestDoc2VecModel",
        testname="test_training_fromfile",
        skip=True,  # cant run in parallel pickle error
        # borntobeflaky/tool/scripts/azure/results/run_16-08-20_17_pytorch/logs/optim_1597697903_gensim/run_1597700266/assert_7101337_10_2/output_0
        params=[
            Param(
                name="epoch1",
                param_line=457,
                param_col=73,
                param_type=ParamType.ITER,
                default_val=20,
                value_range=[1, 20],
                steps=1
            ),
            Param(
                name="epoch2",
                param_line=464,
                param_col=98,
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
                line=428,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(model.dv.doesnt_match([fire1, alt1, fire2]), alt1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="tensor2tensor",
        filename="{0}/projects/tensor2tensor/tensor2tensor/data_generators/text_encoder_test.py".format(
            libraries.PROJECT_DIR),
        classname="SubwordTextEncoderTest",
        testname="test_long_tokens",
        skip=True,  # assertion not suitable
        params=[
            Param(
                name="num_tokens",
                param_line=185,
                param_col=17,
                param_type=ParamType.ITER,
                default_val=50,
                value_range=[1, 50],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/tensor2tensor/tensor2tensor/data_generators/text_encoder_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=209,
                col_offset=-1,
                assert_type=AssertType.ASSERTTRUE,
                assert_string="self.assertTrue(alphabet.issubset(encoder._alphabet))",
                args=[]
            )
        ]


    ),
    Spec(
        repo="tensor2tensor",
        filename="{0}/projects/tensor2tensor/tensor2tensor/data_generators/text_encoder_test.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_run_cv_evaluation_with_response_selector",
        skip=True,
        params=[
            Param(
                name="epochs_DIETClassifier",
                param_line=395,
                param_col=51,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2]
            ),
            Param(
                name="epochs_ResponseSelector",
                param_line=396,
                param_col=53,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/rasa/tests/nlu/test_evaluation.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=428,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert len(entity_results.test[\"DIETClassifier\"][\"F1-score\"]) == n_folds",
                args=[]
            )
        ]


    ),
    Spec(
        repo="rasa",
        filename="{0}/projects/rasa/tests/nlu/test_evaluation.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_run_cv_evaluation_with_response_selector",
        params=[
            Param(
                name="epochs_DIETClassifier",
                param_line=395,
                param_col=51,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2]
            ),
            Param(
                name="epochs_ResponseSelector",
                param_line=396,
                param_col=53,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/rasa/tests/nlu/test_evaluation.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=428,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert len(entity_results.test[\"DIETClassifier\"][\"F1-score\"]) == n_folds",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_simple_ppo",
        # skip=True,# cant handle assert all(.. for ..)
        # /home/saikat/projects/borntobeflaky/tool/scripts/azure/results/run_16-08-20_17_pytorch/logs/optim_1597697884_ml-agents/run_1597697884
        params=[
            Param(
                name="ppo_config_LR",
                param_line=47,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            ),
            Param(
                name="max_steps",
                param_line=54,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=3000,
                value_range=[100, 3000]
            )
        ],
        assertions=[
            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_2d_ppo",
        params=[
            Param(
                name="ppo_config_LR",
                param_line=47,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="batch_size",
                param_line=171,
                param_col=47,
                param_type=ParamType.CHAINS,
                default_val=64,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
            ),
            Param(
                name="max_steps",
                param_line=173,
                param_col=80,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000],
                steps=100
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_visual_ppo",
        params=[
            Param(
                name="learning_rate",
                param_line=187,
                param_col=76,
                param_type=ParamType.LR,
                default_val=3.0e-4,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=54,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=3000,
                value_range=[100, 3000]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )
        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_visual_advanced_ppo",
        params=[
            Param(
                name="learning_rate",
                param_line=206,
                param_col=76,
                param_type=ParamType.LR,
                default_val=3.0e-4,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=211,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[10, 500]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_recurrent_ppo",
        params=[
            Param(
                name="learning_rate",
                param_line=226,
                param_col=50,
                param_type=ParamType.LR,
                default_val=1.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=232,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            )
            # removing batch_size. No other batch size works
            # ,
            # Param(
            #     name="batch_size",
            #     param_line=226,
            #     param_col=69,
            #     param_type=ParamType.CHAINS,
            #     default_val=64,
            #     value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            # )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_simple_sac",
        params=[
            Param(
                name="learning_rate",
                param_line=61,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="batch_size",
                param_line=63,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=8,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            ),
            Param(
                name="max_steps",
                param_line=71,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            )


        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_2d_sac",
        params=[
            Param(
                name="learning_rate",
                param_line=61,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="batch_size",
                param_line=63,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=8,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            ),
            Param(
                name="max_steps",
                param_line=250,
                param_col=80,
                param_type=ParamType.ITER,
                default_val=10000,
                value_range=[100, 10000]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_visual_sac",
        params=[
            Param(
                name="batch_size",
                param_line=265,
                param_col=47,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            ),
            Param(
                name="learning_rate",
                param_line=265,
                param_col=65,
                param_type=ParamType.LR,
                default_val=3.0e-4,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=71,
                param_col=14,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_visual_advanced_sac",
        params=[
            Param(
                name="learning_rate",
                param_line=288,
                param_col=22,
                param_type=ParamType.LR,
                default_val=3.0e-4,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="batch_size",
                param_line=287,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            ),
            Param(
                name="max_steps",
                param_line=295,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=100,
                value_range=[10, 100]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_recurrent_sac",
        params=[
            Param(
                name="learning_rate",
                param_line=314,
                param_col=22,
                param_type=ParamType.LR,
                default_val=1e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=322,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=5000,
                value_range=[100, 5000]
            ),
            Param(
                name="batch_size",
                param_line=313,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=128,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256, 512]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_simple_ghost",
        params=[
            Param(
                name="ppo_config_LR",
                param_line=47,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=335,
                param_col=77,
                param_type=ParamType.ITER,
                default_val=2500,
                value_range=[100, 2500]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )
        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_simple_ghost_fails",
        skip=True,  # weird assertion
        #  assert any(reward > success_threshold for reward in processed_rewards) and any(
        #         reward < success_threshold for reward in processed_rewards
        #     )
        params=[
            Param(
                name="ppo_config_LR",
                param_line=47,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=349,
                param_col=77,
                param_type=ParamType.ITER,
                default_val=2500,
                value_range=[100, 2500]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_simple_asymm_ghost",
        params=[
            Param(
                name="ppo_config_LR",
                param_line=47,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=373,
                param_col=77,
                param_type=ParamType.ITER,
                default_val=4000,
                value_range=[100, 4000]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_simple_asymm_ghost_fails",
        skip=True,  # weird assert
        params=[
            Param(
                name="ppo_config_LR",
                param_line=47,
                param_col=22,
                param_type=ParamType.LR,
                default_val=5.0e-3,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=392,
                param_col=77,
                param_type=ParamType.ITER,
                default_val=4000,
                value_range=[100, 4000]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=400,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_gail_visual_ppo",
        params=[
            Param(
                name="ppo_config_LR",
                param_line=468,
                param_col=72,
                param_type=ParamType.LR,
                default_val=3e-4,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=474,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="batch_size",
                param_line=49,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="ml-agents",
        filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_gail_visual_sac",
        params=[
            Param(
                name="sac_config_LR",
                param_line=494,
                param_col=50,
                param_type=ParamType.LR,
                default_val=3e-4,
                value_range=[1e-5, 1.0]
            ),
            Param(
                name="max_steps",
                param_line=501,
                param_col=18,
                param_type=ParamType.ITER,
                default_val=500,
                value_range=[100, 500]
            ),
            Param(
                name="batch_size",
                param_line=494,
                param_col=67,
                param_type=ParamType.CHAINS,
                default_val=16,
                value_range=[2, 4, 8, 16, 32, 64, 128, 256]
            )
        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/ml-agents/ml-agents/mlagents/trainers/tests/test_simple_rl.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=155,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert all(reward > success_threshold for reward in processed_rewards)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pytorch-lightning",
        filename="{0}/projects/pytorch-lightning/tests/callbacks/test_model_checkpoint.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_model_checkpoint_no_extraneous_invocations",
        skip=True,
        params=[
            Param(
                name="num_epochs",
                param_line=85,
                param_col=17,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/pytorch-lightning/tests/callbacks/test_model_checkpoint.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=96,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert 1 == result",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pytorch-lightning",
        filename="{0}/projects/pytorch-lightning/tests/trainer/test_trainer.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_trainer_min_steps_and_epochs",
skip=True,
        params=[
            Param(
                name="num_epochs",
                param_line=486,
                param_col=19,
                param_type=ParamType.CHAINS,
                default_val=7,
                value_range=[1, 2, 3, 4, 5, 7]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/pytorch-lightning/tests/trainer/test_trainer.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=510,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert trainer.global_step >= math.floor(num_train_samples * 1.5)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="pytorch-lightning",
        filename="{0}/projects/pytorch-lightning/tests/models/test_grad_norm.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_grad_tracking",
skip=True,
        params=[
            Param(
                name="max_epochs",
                param_line=59,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=3,
                value_range=[1, 2, 3]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/pytorch-lightning/tests/models/test_grad_norm.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=75,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert np.allclose(log, mod, rtol=rtol)",
                args=[]
            )
        ]


    ),

    Spec(
        repo="imbalanced-learn",
        filename="{0}/projects/imbalanced-learn/imblearn/ensemble/tests/test_forest.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_balanced_random_forest",
        params=[
            Param(
                name="n_estimators",
                param_line=65,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/imbalanced-learn/imblearn/ensemble/tests/test_forest.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=74,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert len(brf.feature_importances_) == imbalanced_dataset[0].shape[1]",
                args=[]
            )
        ]


    ),
    Spec(
        repo="imbalanced-learn",
        filename="{0}/projects/imbalanced-learn/imblearn/ensemble/tests/test_forest.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_balanced_random_forest_oob",
        params=[
            Param(
                name="n_estimators",
                param_line=119,
                param_col=53,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="min_samples_leaf",
                param_line=120,
                param_col=25,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, 3, 4, 5, 6]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/imbalanced-learn/imblearn/ensemble/tests/test_forest.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=126,
                col_offset=-1,
                assert_type=AssertType.ASSERT,
                assert_string="assert abs(test_score - est.oob_score_) < 0.1",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/training_test.py".format(
            libraries.PROJECT_DIR),
        classname="TrainingTest",
        testname="test_policytrainer_save_restore",
        params=[
            Param(
                name="max_steps",
                param_line=45,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/training_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=110,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(trainer4._policy_trainer.step, 4)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/training_test.py".format(
            libraries.PROJECT_DIR),
        classname="TrainingTest",
        testname="test_policytrainer_cartpole",
        params=[
            Param(
                name="max_steps",
                param_line=119,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[10, 200]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/training_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=142,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(trainer.current_epoch, ep + 1)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticTest",
        testname="test_a2ctrainer_save_restore",
        params=[
            Param(
                name="max_steps",
                param_line=43,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=20,
                value_range=[1, 20],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/training_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=82,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(trainer2._policy_trainer.step, 6)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticTest",
        testname="test_sanity_ppo_cartpole",
        params=[
            Param(
                name="max_steps",
                param_line=115,
                param_col=57,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[1, 200]
            ),
            Param(
                name="lr",
                param_line=118,
                param_col=17,
                param_type=ParamType.LR,
                default_val=1e-3,
                value_range=[1e-3, 1.0]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=141,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(2, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticTest",
        testname="test_awrtrainer_cartpole",
        params=[
            Param(
                name="max_steps",
                param_line=146,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[1, 200]
            ),
            Param(
                name="lr",
                param_line=151,
                param_col=17,
                param_type=ParamType.LR,
                default_val=1e-2,
                value_range=[1e-2, 1.0]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=173,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(1, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticTest",
        testname="test_awrtrainer_cartpole_shared",
        params=[
            Param(
                name="max_steps",
                param_line=184,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[1, 200]
            ),
            Param(
                name="lr",
                param_line=191,
                param_col=21,
                param_type=ParamType.LR,
                default_val=1e-2,
                value_range=[1e-2, 1.0]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=216,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(1, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticTest",
        testname="test_sampling_awrtrainer_cartpole",
        params=[
            Param(
                name="max_steps",
                param_line=257,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=20,
                value_range=[1, 20],
                steps=1
            ),
            Param(
                name="lr",
                param_line=262,
                param_col=17,
                param_type=ParamType.LR,
                default_val=1e-2,
                value_range=[1e-2, 1.0]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=285,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(1, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticTest",
        testname="test_sampling_awrtrainer_cartpole_sample_all_discrete",
        params=[
            Param(
                name="max_steps",
                param_line=290,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=20,
                value_range=[1, 20],
                steps=1
            ),
            Param(
                name="lr",
                param_line=295,
                param_col=17,
                param_type=ParamType.LR,
                default_val=1e-2,
                value_range=[1e-2, 1.0]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=318,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(1, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticJointTest",
        testname="test_awrjoint_save_restore",
        params=[
            Param(
                name="max_steps",
                param_line=42,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[1, 200]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=70,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(trainer2._trainer.step, 3)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticJointTest",
        testname="test_jointppotrainer_cartpole",
        params=[
            Param(
                name="batch_size",
                param_line=92,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=4,
                value_range=[1, 4],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=96,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(2, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticJointTest",
        testname="test_jointawrtrainer_cartpole",
        params=[
            Param(
                name="max_steps",
                param_line=101,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[1, 200]
            ),
            Param(
                name="batch_size",
                param_line=113,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=4,
                value_range=[1, 4],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=117,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(2, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticJointTest",
        testname="test_jointa2ctrainer_cartpole",
        params=[
            Param(
                name="max_steps",
                param_line=122,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[1, 200]
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=138,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(2, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="trax",
        filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
            libraries.PROJECT_DIR),
        classname="ActorCriticJointTest",
        testname="test_jointa2ctrainer_cartpole",
        params=[
            Param(
                name="max_steps",
                param_line=161,
                param_col=36,
                param_type=ParamType.ITER,
                default_val=200,
                value_range=[1, 200]
            ),
            Param(
                name="batch_size",
                param_line=169,
                param_col=19,
                param_type=ParamType.ITER,
                default_val=4,
                value_range=[1, 4],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/trax/trax/rl/actor_critic_joint_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=173,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(2, trainer.current_epoch)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="bambi",
        filename="{0}/projects/bambi/bambi/tests/test_built_models.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_logistic_regression",
        params=[
            Param(
                name="samples",
                param_line=379,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="chains",
                param_line=379,
                param_col=29,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4]
            ),
            Param(
                name="samples2",
                param_line=400,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=1000,
                value_range=[100, 1000]
            ),
            Param(
                name="chains2",
                param_line=400,
                param_col=29,
                param_type=ParamType.CHAINS,
                default_val=4,
                value_range=[1, 2, 3, 4]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="test_logistic_regression",
                          classname="none",
                          filename="{0}/projects/bambi/bambi/tests/test_built_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=43,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(a[x], b[x], atol=0, rtol=0.01)",
                args=[]
            )
        ]
    ),
    Spec(
        repo="bambi",
        filename="{0}/projects/bambi/bambi/tests/test_built_models.py".format(
            libraries.PROJECT_DIR),
        classname="none",
        testname="test_many_fixed_many_random",
        params=[
            Param(
                name="samples",
                param_line=207,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            ),
            Param(
                name="samples",
                param_line=208,
                param_col=16,
                param_type=ParamType.ITER,
                default_val=10,
                value_range=[1, 10],
                steps=1
            ),
            Param(
                name="chains",
                param_line=209,
                param_col=15,
                param_type=ParamType.CHAINS,
                default_val=2,
                value_range=[1, 2, 3, 4]
            )

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="test_logistic_regression",
                          classname="none",
                          filename="{0}/projects/bambi/bambi/tests/test_built_models.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=43,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="np.testing.assert_allclose(a[x], b[x], atol=0, rtol=0.01)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="dopamine",
        filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
            libraries.PROJECT_DIR),
        classname="OutOfGraphReplayBufferTest",
        testname="testGetRangeNoWraparound",
        skip=True,
        params=[
            Param(
                name="batch_size",
                param_line=38,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=32,
                value_range=[1, 32],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=218,
                col_offset=-1,
                assert_type=AssertType.ASSERTALLEQUAL,
                assert_string="self.assertAllEqual(sliced_array, array[2:5])",
                args=[]
            )
        ]


    ),
    Spec(
        repo="dopamine",
        filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
            libraries.PROJECT_DIR),
        classname="OutOfGraphReplayBufferTest",
        testname="testGetRangeWithWraparound",
        skip=True,
        params=[
            Param(
                name="batch_size",
                param_line=38,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=32,
                value_range=[1, 32],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=250,
                col_offset=-1,
                assert_type=AssertType.ASSERTALLEQUAL,
                assert_string="self.assertAllEqual(sliced_array, rolled_array[:4])",
                args=[]
            )
        ]


    ),
    Spec(
        repo="dopamine",
        filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
            libraries.PROJECT_DIR),
        classname="OutOfGraphReplayBufferTest",
        testname="testNSteprewardum",
        skip=True,
        params=[
            Param(
                name="batch_size",
                param_line=38,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=32,
                value_range=[1, 32],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=269,
                col_offset=-1,
                assert_type=AssertType.ASSERTEQUAL,
                assert_string="self.assertEqual(batch[2][0], 10.0)",
                args=[]
            )
        ]


    ),
    Spec(
        repo="dopamine",
        filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
            libraries.PROJECT_DIR),
        classname="OutOfGraphReplayBufferTest",
        testname="testSave",
        skip=True,
        params=[
            Param(
                name="batch_size",
                param_line=38,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=32,
                value_range=[1, 32],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=297,
                col_offset=-1,
                assert_type=AssertType.ASSERTTRUE,
                assert_string="self.assertTrue(tf.io.gfile.exists(filename))",
                args=[]
            )
        ]

    ),
    Spec(
        repo="dopamine",
        filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
            libraries.PROJECT_DIR),
        classname="OutOfGraphReplayBufferTest",
        testname="testSave",
        skip=True,
        params=[
            Param(
                name="batch_size",
                param_line=38,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=32,
                value_range=[1, 32],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=526,
                col_offset=-1,
                assert_type=AssertType.ASSERTTRUE,
                assert_string="self.assertTrue(tf.io.gfile.exists(filename))",
                args=[]
            )
        ]

    ),
    Spec(
        repo="dopamine",
        filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
            libraries.PROJECT_DIR),
        classname="WrappedReplayBufferTest",
        testname="testWrapperLoad",
        skip=True,  # fails locally
        params=[
            Param(
                name="batch_size",
                param_line=38,
                param_col=13,
                param_type=ParamType.ITER,
                default_val=32,
                value_range=[1, 32],
                steps=1
            ),

        ],
        assertions=[

            AssertSpec(
                test=Test(testname="none",
                          classname="none",
                          filename="{0}/projects/dopamine/tests/dopamine/replay_memory/circular_replay_buffer_test.py".format(
                              libraries.PROJECT_DIR)
                          ),
                line=806,
                col_offset=-1,
                assert_type=AssertType.ASSERT_ALLCLOSE,
                assert_string="self.assertAllClose(replay.memory.invalid_range, self._test_invalid_range)",
                args=[]
            )
        ]

    )



]
