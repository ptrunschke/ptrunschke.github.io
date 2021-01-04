---
layout: page
title: "Projects"
permalink: /projects/
author: Philipp Trunschke
---

<style>
#papers {
  width: 100%;
  margin-bottom: 1em;
}
#papers th {
  padding: 0.60em;
  padding-top: 0;
  height: 2em;
}
#papers .date {
  text-align: left;
}
#papers .author {
  text-align: center;
}
#papers td {
  padding: 0.3em;
  height: 1.8em;
  vertical-align: top;
}
#papers td.date {
  padding: 0.3em 0;
}
</style>

Paper Club
----

The <em>&laquo;Paper Club&raquo;</em> is a small circle of interested students meeting once
a month to read and discuss papers from diverse scientific fields.
The following table serves as a reference and lists the papers we have read in previous meetings.

<table id="papers">
<colgroup>
    <col width="22%">
	<col width="33%">
	<col width="45%">
</colgroup>
<tbody>

<tr>
    <th class="date"> Date </th>
    <th class="author"> Authors </th>
    <th> Title </th>
</tr>

<tr>
    <td class="date"> September 25, 2017 </td>
    <td class="author"> Guy Katz, Clark Barrett, David Dill, Kyle Julian, Mykel Kochenderfer </td>
    <td> <a href="https://arxiv.org/abs/1702.01135"> Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks </a> </td>
</tr>

<tr>
    <td class="date"> October 27, 2017 </td>
    <td class="author"> Martin Gander, Gerhard Wanner </td>
    <td> <a href="https://epubs.siam.org/doi/abs/10.1137/100804036"> From Euler, Ritz, and Galerkin to Modern Computing </a> </td>
</tr>

<tr>
    <td class="date"> December 4, 2017 </td>
    <td class="author"> Satoshi Nakamoto </td>
    <td> <a href="https://bitcoin.org/bitcoin.pdf"> Bitcoin: A Peer-to-Peer Electronic Cash System </a> </td>
</tr>

<tr>
    <td class="date"> January 3, 2018 </td>
    <td class="author"> Tianqi Chen, Carlos Guestrin </td>
    <td> <a href="https://arxiv.org/abs/1603.02754"> XGBoost: A Scalable Tree Boosting System </a> </td>
</tr>

<tr>
    <td class="date"> January 29, 2018 </td>
    <td class="author"> Miguel Alcubierre </td>
    <td> <a href="https://arxiv.org/abs/gr-qc/0009013"> The warp drive: hyper-fast travel within general relativity </a> </td>
</tr>

<tr>
    <td class="date"> March 7, 2018 </td>
    <td class="author"> Maurizio Falcone, Roberto Ferretti </td>
    <td> <a href="https://doi.org/10.1137/1.9781611973051.ch8"> Semi-Lagrangian Approximation Schemes for Linear and Hamilton-Jacobi Equations &mdash; Chapter 8: Control and games </a> </td>
</tr>

<tr>
    <td class="date"> April 11, 2018 </td>
    <td class="author"> Dave Bayer, Persi Diaconis </td>
    <td> <a href="http://statweb.stanford.edu/~cgates/PERSI/papers/bayer92.pdf"> Trailing the Dovetail Shuffle to its Lair </a> (I) </td>
</tr>

<tr>
    <td class="date"> May 1, 2018 </td>
    <td class="author"> Dave Bayer, Persi Diaconis </td>
    <td> <a href="http://statweb.stanford.edu/~cgates/PERSI/papers/bayer92.pdf"> Trailing the Dovetail Shuffle to its Lair </a> (II) </td>
</tr>

</tbody>
</table>


PAPP<a name="PAPP"></a>
----
Project AFEM Plus Plus (PAPP) is aimed at implementing a fast, yet practical FEM library written in C++.
It allows

- fast adaptive n-dimensional refinements
- an easy way to extend the library (custom refinement schemes/finite elements)
- an easy to use FFI

<a href="https://www.math.hu-berlin.de/~bethke" target="blank">Lead developer</a><br>
<a href="https://www.math.hu-berlin.de/~bethke/Projects/PAPP/index.html" target="blank">Documentation</a>


Xerus<a name="Xerus"></a>
----
The `xerus` library is a general purpose library for numerical calculations with higher order tensors, Tensor-Train Decompositions and general Tensor Networks. The focus of development was the simple usability and adaptibility to any setting that requires higher order tensors or decompositions thereof.

- Modern code and concepts incorporating many features of the C++11 standard.
- Full python bindings with very similar syntax for easy transitions from and to C++.
- Calculation with tensors of arbitrary orders using an intuitive Einstein-like notation `A(i,j) = B(i,k,l) * C(k,j,l);`.
- Full implementation of the Tensor-Train decompositions (MPS) with all neccessary capabilities (including Algorithms like ALS, ADF and CG).
- Lazy evaluation of (multiple) tensor contractions featuring heuristics to automatically find efficient contraction orders.
- Direct integration of the blas and lapack, as high performance linear algebra backends.
- Fast sparse tensor calculation by usage of the suiteSparse sparse matrix capabilities.
- Capabilites to handle arbitrary Tensor Networks.

[Project Home-Page](https://libxerus.org/)


<!--
<div style="height: 1em"></div>

Github <a name="Github"></a>
------
Host all your stuff there

- Short intro to Sphinx
- Gaslab simulator
- Bachelor thesis
- The project with vera?
- prompt/scripts
-->
