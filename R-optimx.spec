#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-optimx
Version  : 2021.10.12
Release  : 36
URL      : https://cran.r-project.org/src/contrib/optimx_2021-10.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/optimx_2021-10.12.tar.gz
Summary  : Expanded Replacement and Extension of the 'optim' Function
Group    : Development/Tools
License  : GPL-2.0
Requires: R-numDeriv
BuildRequires : R-numDeriv
BuildRequires : buildreq-R

%description
function to call to several function minimization codes in R in a single
    statement. These methods handle smooth, possibly box constrained functions 
    of several or many parameters. Note that function 'optimr()' was prepared to
    simplify the incorporation of minimization codes going forward. Also implements some
    utility codes and some extra solvers, including safeguarded Newton methods.
    Many methods previously separate are now included here.
    This is the version for CRAN.

%prep
%setup -q -c -n optimx
cd %{_builddir}/optimx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634223120

%install
export SOURCE_DATE_EPOCH=1634223120
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optimx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optimx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optimx
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc optimx || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/optimx/CITATION
/usr/lib64/R/library/optimx/DESCRIPTION
/usr/lib64/R/library/optimx/INDEX
/usr/lib64/R/library/optimx/Meta/Rd.rds
/usr/lib64/R/library/optimx/Meta/demo.rds
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
/usr/lib64/R/library/optimx/demo/brown_test.R
/usr/lib64/R/library/optimx/demo/brown_testRV.R
/usr/lib64/R/library/optimx/demo/broydt_test.R
/usr/lib64/R/library/optimx/demo/chen_test.R
/usr/lib64/R/library/optimx/demo/chenlog_test.R
/usr/lib64/R/library/optimx/demo/cyq_test.R
/usr/lib64/R/library/optimx/demo/froth_test.R
/usr/lib64/R/library/optimx/demo/genrose_test.R
/usr/lib64/R/library/optimx/demo/maxtestJN.R
/usr/lib64/R/library/optimx/demo/onepar_test.R
/usr/lib64/R/library/optimx/demo/ox.R
/usr/lib64/R/library/optimx/demo/poissmix_test.R
/usr/lib64/R/library/optimx/demo/rosbkext_test.R
/usr/lib64/R/library/optimx/demo/sc2_test.R
/usr/lib64/R/library/optimx/demo/trig_test.R
/usr/lib64/R/library/optimx/demo/unit1.R
/usr/lib64/R/library/optimx/demo/unitTests.R
/usr/lib64/R/library/optimx/demo/valley_test.R
/usr/lib64/R/library/optimx/demo/vmmix_test.R
/usr/lib64/R/library/optimx/doc/Extend-optimx-code.R
/usr/lib64/R/library/optimx/doc/Extend-optimx.R
/usr/lib64/R/library/optimx/doc/Extend-optimx.Rmd
/usr/lib64/R/library/optimx/doc/Extend-optimx.pdf
/usr/lib64/R/library/optimx/doc/Rvmmin-code.R
/usr/lib64/R/library/optimx/doc/Rvmmin.R
/usr/lib64/R/library/optimx/doc/Rvmmin.Rmd
/usr/lib64/R/library/optimx/doc/Rvmmin.html
/usr/lib64/R/library/optimx/doc/SNewton-code.R
/usr/lib64/R/library/optimx/doc/SNewton.R
/usr/lib64/R/library/optimx/doc/SNewton.Rmd
/usr/lib64/R/library/optimx/doc/SNewton.html
/usr/lib64/R/library/optimx/doc/index.html
/usr/lib64/R/library/optimx/help/AnIndex
/usr/lib64/R/library/optimx/help/aliases.rds
/usr/lib64/R/library/optimx/help/optimx.rdb
/usr/lib64/R/library/optimx/help/optimx.rdx
/usr/lib64/R/library/optimx/help/paths.rds
/usr/lib64/R/library/optimx/html/00Index.html
/usr/lib64/R/library/optimx/html/R.css
/usr/lib64/R/library/optimx/tests/bdstest.R
/usr/lib64/R/library/optimx/tests/hobbs.R
/usr/lib64/R/library/optimx/tests/jonesrun.R
/usr/lib64/R/library/optimx/tests/maxfn.R
/usr/lib64/R/library/optimx/tests/rosenbrock.R
/usr/lib64/R/library/optimx/tests/run1param.R
/usr/lib64/R/library/optimx/tests/simplefuntst.R
/usr/lib64/R/library/optimx/tests/snsimple.R
/usr/lib64/R/library/optimx/tests/snwood.R
/usr/lib64/R/library/optimx/tests/ssqbtest.R
/usr/lib64/R/library/optimx/tests/tfnchk.R
/usr/lib64/R/library/optimx/tests/tgrchk.R
/usr/lib64/R/library/optimx/tests/tkktc.R
/usr/lib64/R/library/optimx/tests/trig1507.R
