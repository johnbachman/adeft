from adeft.score.score import OptimizationTestCase, StitchTestCase, \
    PermSearchTestCase


def test_perm_search():
    case1 = PermSearchTestCase(candidates=[[1], [1, 0], [1, 1, 0], [1, 1],
                                           [0]],
                               shortform=[0, 1],
                               indices=[[0], [0, 1], [0, 1, 2],
                                       [0, 1], [0]],
                               penalties=[0.4, 0.2],
                               word_prizes=[1.0]*5,
                               word_penalties=[1.0, 2.0, 3.0, 4.0, 5.0],
                               alpha=0.5,
                               beta=0.8,
                               gamma=0.85,
                               lambda_=0.75,
                               rho=0.9,
                               len_perm=5,
                               result_score=(2/5)**(1/4) * (9/10))
    case2 = PermSearchTestCase(candidates=[[0, 1, 0], [1, 0, 0, 1]],
                               shortform=[0, 1],
                               indices=[[0, 3, 5],
                                       [0, 1, 3, 6]],
                               penalties=[1.0, 0.4],
                               word_prizes=[1.0, 1.0],
                               word_penalties=[1.0, 2.0],
                               alpha=0.5,
                               beta=0.8,
                               gamma=0.85,
                               lambda_=0.6,
                               rho=0.9,
                               len_perm=2,
                               result_score=1.0)
    for case in [case1, case2]:
        case.run_test()


def test_make_candidates_array():
    case1 = StitchTestCase(candidates=[[0], [0, 1], [1, 1, 0], [0, 0], [1]],
                           indices=[[0], [0, 1], [0, 1, 2],
                                   [0, 1], [0]],
                           word_prizes=[1., 0.9, 0.8, 0.7, 0.6],
                           W_array=[0.6, 1.3, 2.1, 3., 4.],
                           permutation=[2, 0, 1, 3, 4],
                           result_x=[-1, 1, -1, 1, -1, 0, -1, 0, -1, 0,
                                     -1, 1, -1, 0, -1, 0, -1, 1, -1],
                           result_indices=[-1, 0, -1, 1, -1, 2,
                                          -1, 0, -1, 0, -1, 1, -1,
                                           0, -1, 1, -1, 0, -1],
                           result_word_prizes=[0.8, 1., 0.9, 0.7, 0.6],
                           result_word_boundaries=[6, 8, 12, 16, 18])

    case2 = StitchTestCase(candidates=[[0], [0, 1], [1, 1, 0], [0, 0], [1]],
                           indices=[[0], [0, 1], [0, 1, 2],
                                   [0, 1], [0]],
                           word_prizes=[1., 0.9, 0.8, 0.7, 0.6],
                           W_array=[0.6, 1.3, 2.1, 3., 4.],
                           permutation=[2, 0, 1],
                           result_x=[-1, 1, -1, 1, -1, 1, -1, 0, -1, 0,
                                     -1, 0, -1],
                           result_indices=[-1, 0, -1, 0, -1, 1,
                                          -1, 2, -1, 0, -1, 1, -1],
                           result_word_prizes=[0.6, 0.8, 0.7],
                           result_word_boundaries=[2, 8, 12])

    cases = [case1, case2]
    for case in cases:
        case.run_test()


def test_optimize():
    case1 = OptimizationTestCase(x=[-1, 0, -1, 1, -1, 0, -1],
                                 y=[0, 1],
                                 indices=[-1, 0, -1, 0, -1, 1, -1],
                                 penalties=[0.4, 0.2],
                                 word_boundaries=[2, 6],
                                 word_prizes=[1, 1],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.75,
                                 W=2.,
                                 result_score=1.0,
                                 result_char_scores=[1., 1.])

    case2 = OptimizationTestCase(x=[-1, 0, -1, 0, -1, 1, -1, 1, -1],
                                 y=[0, 1],
                                 indices=[-1, 0, -1, 1, -1,
                                          2, -1, 3, -1],
                                 penalties=[0.4, 0.2],
                                 word_boundaries=[8],
                                 word_prizes=[1],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.75,
                                 W=1.,
                                 result_score=(1.8/2)**(3/4),
                                 result_char_scores=[1.0, 0.8])

    case3 = OptimizationTestCase(x=[-1, 0, -1, 1, -1, 0, -1, 0, -1, 1, -1],
                                 y=[0, 1],
                                 indices=[-1, 0, -1, 0, -1, 0, -1, 1,
                                         -1, 2, -1],
                                 penalties=[0.4, 0.2],
                                 word_boundaries=[2, 4, 10],
                                 word_prizes=[0.5, 0.5, 2.0],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.5,
                                 W=3.0,
                                 result_score=(1.8/2)**(1/2)*(2/3)**(1/2),
                                 result_char_scores=[1.0, 0.8])

    case4 = OptimizationTestCase(x=[-1, 0, -1, 1, -1, 0, -1, 0, -1, 1, -1],
                                 y=[0, 1],
                                 indices=[-1, 0, -1, 0, -1, 0, -1, 1,
                                          -1, 2, -1],
                                 penalties=[0.4, 0.2],
                                 word_boundaries=[2, 4, 10],
                                 word_prizes=[0.5, 0.5, 1.25],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.75,
                                 W=2.25,
                                 result_score=(2/3)**(1/2),
                                 result_char_scores=[1., 1.])

    case5 = OptimizationTestCase(x=[-1, 0, -1, 1, -1, 0, -1, 0, -1, 1, -1],
                                 y=[0, 1],
                                 indices=[-1, 0, -1, 0, -1, 0, -1, 1,
                                          -1, 2, -1],
                                 penalties=[0.4, 0.2],
                                 word_boundaries=[2, 4, 10],
                                 word_prizes=[0.5, 0.5, 1],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.75,
                                 W=2.5,
                                 result_score=(2/5)**(1/4),
                                 result_char_scores=[1., 1.])

    # Two words. Only one character in shortform matches
    case6 = OptimizationTestCase(x=[-1, 0, -1, 0, -1],
                                 y=[0, 1],
                                 indices=[-1, 0, -1, 0, -1],
                                 penalties=[0.4, 0.2],
                                 word_boundaries=[2, 4],
                                 word_prizes=[1., 0.5],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.75,
                                 W=1.5,
                                 result_score=(2/5)**(3/4)*(2/3)**(1/4),
                                 result_char_scores=[1., -0.2])

    # INDRA with tokens permuted
    char_score = (3 + 0.8**4 - 0.4**2)/5
    case7 = OptimizationTestCase(x=[-1, 4, -1, 3, -1, 3, -1, 4, -1, 1, -1,
                                    0, -1, 1, -1, 2, -1, 1, -1, 4, -1, 0, -1,
                                    4, -1, 0, -1, 1, -1, 3, -1, 4, -1, 2, -1,
                                    1, -1, 3, -1, 4, -1, 1, -1, 2, -1],
                                 y=[0, 1, 2, 3, 4],
                                 indices=[-1, 0, -1, 8, -1, 0,
                                          -1, 2, -1, 5, -1,
                                          6, -1, 7, -1, 0,
                                          -1, 2, -1, 3, -1, 5,
                                          -1, 7, -1, 0, -1, 1,
                                          -1, 5, -1, 6, -1,
                                          9, -1, 0, -1, 5,
                                          -1, 0, -1, 1, -1, 2, -1],
                                 penalties=[0.4**i for i in range(5)],
                                 word_boundaries=[4, 14, 24, 34, 38, 44],
                                 word_prizes=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.6,
                                 W=6.0,
                                 result_score=(char_score)**0.6*(1/2)**0.4,
                                 result_char_scores=[1., 1., -0.4**2,
                                                     0.8**4, 1.])

    # Estrogen Receptor (ER)
    case8 = OptimizationTestCase(x=[-1, 0, -1, 1, -1, 0, -1, 1, -1, 0, -1, 0,
                                    -1, 1, -1],
                                 y=[0, 1],
                                 indices=[-1, 0, -1, 3, -1, 5, -1, 0, -1, 1,
                                          -1, 4, -1, 6, -1],
                                 penalties=[1.0, 0.4],
                                 word_boundaries=[6, 14],
                                 word_prizes=[1.0, 1.0],
                                 alpha=0.5,
                                 beta=0.8,
                                 gamma=0.85,
                                 lambda_=0.6,
                                 W=2.0,
                                 result_score=1.0,
                                 result_char_scores=[1.0, 1.0])

    test_cases = [case1, case2, case3, case4, case5, case6, case7, case8]
    for case in test_cases:
        case.check_assertions()
        case.run_test()
