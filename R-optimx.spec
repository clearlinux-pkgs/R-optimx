#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-optimx
Version  : 2023.8.13
Release  : 47
URL      : https://cran.r-project.org/src/contrib/optimx_2023-8.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/optimx_2023-8.13.tar.gz
Summary  : Expanded Replacement and Extension of the 'optim' Function
Group    : Development/Tools
License  : GPL-2.0
Requires: R-nloptr
Requires: R-numDeriv
Requires: R-pracma
BuildRequires : R-lbfgsb3c
BuildRequires : R-nloptr
BuildRequires : R-numDeriv
BuildRequires : R-pracma
BuildRequires : R-subplex
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
function to call to several function minimization codes in R in a single
    statement. These methods handle smooth, possibly box constrained functions 
    of several or many parameters. Note that function 'optimr()' was prepared to
    simplify the incorporation of minimization codes going forward. Also implements some
    utility codes and some extra solvers, including safeguarded Newton methods.
    Many methods previously separate are now included here.
    This is the version for CRAN.

%prep
%setup -q -n optimx
pushd ..
cp -a optimx buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692060868

%install
export SOURCE_DATE_EPOCH=1692060868
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/optimx/CITATION
/usr/lib64/R/library/optimx/DESCRIPTION
/usr/lib64/R/library/optimx/INDEX
/usr/lib64/R/library/optimx/Meta/Rd.rds
/usr/lib64/R/library/optimx/Meta/features.rds
/usr/lib64/R/library/optimx/Meta/hsearch.rds
/usr/lib64/R/library/optimx/Meta/links.rds
/usr/lib64/R/library/optimx/Meta/nsInfo.rds
/usr/lib64/R/library/optimx/Meta/package.rds
/usr/lib64/R/library/optimx/Meta/vignette.rds
/usr/lib64/R/library/optimx/NAMESPACE
/usr/lib64/R/library/optimx/NEWS
/usr/lib64/R/library/optimx/R/optimx
/usr/lib64/R/library/optimx/R/optimx.rdb
/usr/lib64/R/library/optimx/R/optimx.rdx
/usr/lib64/R/library/optimx/doc/ExplainGradMinR.R
/usr/lib64/R/library/optimx/doc/ExplainGradMinR.Rmd
/usr/lib64/R/library/optimx/doc/ExplainGradMinR.pdf
/usr/lib64/R/library/optimx/doc/Extend-optimx.R
/usr/lib64/R/library/optimx/doc/Extend-optimx.Rmd
/usr/lib64/R/library/optimx/doc/Extend-optimx.pdf
/usr/lib64/R/library/optimx/doc/Extend-optimx20171215.Rmd
/usr/lib64/R/library/optimx/doc/Intro-to-optimx.R
/usr/lib64/R/library/optimx/doc/Intro-to-optimx.Rmd
/usr/lib64/R/library/optimx/doc/Intro-to-optimx.pdf
/usr/lib64/R/library/optimx/doc/Rvmmin.R
/usr/lib64/R/library/optimx/doc/Rvmmin.Rmd
/usr/lib64/R/library/optimx/doc/Rvmmin.pdf
/usr/lib64/R/library/optimx/doc/SNewton.R
/usr/lib64/R/library/optimx/doc/SNewton.Rmd
/usr/lib64/R/library/optimx/doc/SNewton.pdf
/usr/lib64/R/library/optimx/doc/examples/0README.txt
/usr/lib64/R/library/optimx/doc/examples/3Rosen.R
/usr/lib64/R/library/optimx/doc/examples/HessQuality.R
/usr/lib64/R/library/optimx/doc/examples/StyblinskiTang2308.R
/usr/lib64/R/library/optimx/doc/examples/argclash.R
/usr/lib64/R/library/optimx/doc/examples/axsearch-Ex.R
/usr/lib64/R/library/optimx/doc/examples/brown_test.R
/usr/lib64/R/library/optimx/doc/examples/broydt_test.R
/usr/lib64/R/library/optimx/doc/examples/chen_test.R
/usr/lib64/R/library/optimx/doc/examples/chenlog_test.R
/usr/lib64/R/library/optimx/doc/examples/cyq_test.R
/usr/lib64/R/library/optimx/doc/examples/dropnmbk.R
/usr/lib64/R/library/optimx/doc/examples/fhopall.R
/usr/lib64/R/library/optimx/doc/examples/froth_test.R
/usr/lib64/R/library/optimx/doc/examples/genrose_test.R
/usr/lib64/R/library/optimx/doc/examples/hessapptest.R
/usr/lib64/R/library/optimx/doc/examples/hessian-used.R
/usr/lib64/R/library/optimx/doc/examples/hobbs.R
/usr/lib64/R/library/optimx/doc/examples/jonesrun.R
/usr/lib64/R/library/optimx/doc/examples/maxtestJN.R
/usr/lib64/R/library/optimx/doc/examples/ncgtests.R
/usr/lib64/R/library/optimx/doc/examples/onepar_test.R
/usr/lib64/R/library/optimx/doc/examples/optimrgrapprox.R
/usr/lib64/R/library/optimx/doc/examples/ox.R
/usr/lib64/R/library/optimx/doc/examples/poissmix_test.R
/usr/lib64/R/library/optimx/doc/examples/rosbkext_test.R
/usr/lib64/R/library/optimx/doc/examples/rosenbrock.R
/usr/lib64/R/library/optimx/doc/examples/runex.R
/usr/lib64/R/library/optimx/doc/examples/sc2_test.R
/usr/lib64/R/library/optimx/doc/examples/scalechk-Ex.R
/usr/lib64/R/library/optimx/doc/examples/simplefun.R
/usr/lib64/R/library/optimx/doc/examples/simplefuntst.R
/usr/lib64/R/library/optimx/doc/examples/snewtonbtest.R
/usr/lib64/R/library/optimx/doc/examples/specctrlhobbs.R
/usr/lib64/R/library/optimx/doc/examples/ssqtest.R
/usr/lib64/R/library/optimx/doc/examples/trig1507.R
/usr/lib64/R/library/optimx/doc/examples/trystarttests.R
/usr/lib64/R/library/optimx/doc/examples/valley_test.R
/usr/lib64/R/library/optimx/doc/examples/vmmix_test.R
/usr/lib64/R/library/optimx/doc/examples/woodtest.R
/usr/lib64/R/library/optimx/doc/index.html
/usr/lib64/R/library/optimx/doc/legacy-demo/00Index
/usr/lib64/R/library/optimx/doc/legacy-demo/brown_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/brown_testRV.R
/usr/lib64/R/library/optimx/doc/legacy-demo/broydt_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/chen_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/chenlog_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/cyq_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/froth_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/genrose_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/maxtestJN.R
/usr/lib64/R/library/optimx/doc/legacy-demo/onepar_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/ox.R
/usr/lib64/R/library/optimx/doc/legacy-demo/poissmix_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/rosbkext_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/sc2_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/trig_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/valley_test.R
/usr/lib64/R/library/optimx/doc/legacy-demo/vmmix_test.R
/usr/lib64/R/library/optimx/doc/ncg2204.R
/usr/lib64/R/library/optimx/doc/ncgqs2204.R
/usr/lib64/R/library/optimx/doc/optcontrol.xls
/usr/lib64/R/library/optimx/doc/replaced2021/Rcgminb-old.R
/usr/lib64/R/library/optimx/doc/replaced2021/axsearch2018.R
/usr/lib64/R/library/optimx/doc/replaced2023/snewtonm.R
/usr/lib64/R/library/optimx/doc/testefnegr.R
/usr/lib64/R/library/optimx/help/AnIndex
/usr/lib64/R/library/optimx/help/aliases.rds
/usr/lib64/R/library/optimx/help/optimx.rdb
/usr/lib64/R/library/optimx/help/optimx.rdx
/usr/lib64/R/library/optimx/help/paths.rds
/usr/lib64/R/library/optimx/html/00Index.html
/usr/lib64/R/library/optimx/html/R.css
/usr/lib64/R/library/optimx/tests/argclash.R
/usr/lib64/R/library/optimx/tests/bdstest.R
/usr/lib64/R/library/optimx/tests/exrosen.R
/usr/lib64/R/library/optimx/tests/maxfn.R
/usr/lib64/R/library/optimx/tests/maxtest.R
/usr/lib64/R/library/optimx/tests/run1param.R
/usr/lib64/R/library/optimx/tests/tfnchk.R
/usr/lib64/R/library/optimx/tests/tgrchk.R
/usr/lib64/R/library/optimx/tests/tkktc.R
