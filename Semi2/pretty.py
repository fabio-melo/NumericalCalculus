import numpy as np
from IPython.display import display, HTML

def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

def mat_print_(a, mat):
  return r"""
<html>
<head>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" async
  src="https://example.com/mathjax/MathJax.js?config=TeX-AMS_CHTML">
</script>
</head>
<body>
$$
""" \
  +  f"{a} = " + bmatrix(mat) + r""" $$ </body>
</html>"""


def mat_print(a, mat):
  return display(HTML(mat_print_(a,mat)))
