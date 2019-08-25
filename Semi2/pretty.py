def bmatrix(a):
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)


def mat_print(i, mat):
    return r"$$" + r" x^{(k=" + str(i) + r")} = " + bmatrix(mat) + r""" $$ """


mathjax = r"""<head>
          <script type="text/x-mathjax-config">
            MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
          </script>
          <script type="text/javascript" async
            src="https://example.com/mathjax/MathJax.js?config=TeX-AMS_CHTML">
          </script>
          </head>
          """

def math(i, mat):
    return r"$$" + str(i) + "= " + bmatrix(mat) + r""" $$ """