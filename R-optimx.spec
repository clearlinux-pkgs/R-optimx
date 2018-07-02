#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-optimx
Version  : 2013.8.7
Release  : 3
URL      : https://cran.r-project.org/src/contrib/optimx_2013.8.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/optimx_2013.8.7.tar.gz
Summary  : A Replacement and Extension of the optim() Function
Group    : Development/Tools
License  : GPL-2.0
Requires: R-BB
Requires: R-Rcgmin
Requires: R-Rvmmin
Requires: R-dfoptim
Requires: R-minqa
Requires: R-numDeriv
Requires: R-setRNG
Requires: R-svUnit
Requires: R-ucminf
BuildRequires : R-BB
BuildRequires : R-Rcgmin
BuildRequires : R-Rvmmin
BuildRequires : R-dfoptim
BuildRequires : R-minqa
BuildRequires : R-numDeriv
BuildRequires : R-setRNG
BuildRequires : R-svUnit
BuildRequires : R-ucminf
BuildRequires : clr-R-helpers

%description
function to unify and streamline optimization capabilities in R
    for smooth, possibly box constrained functions of several or
    many parameters. This is the CRAN version of the package.

%prep
%setup -q -c -n optimx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530502860

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530502860
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optimx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optimx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library optimx
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library optimx|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/optimx/demo/froth_test.R
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
/usr/lib64/R/library/optimx/help/AnIndex
/usr/lib64/R/library/optimx/help/aliases.rds
/usr/lib64/R/library/optimx/help/optimx.rdb
/usr/lib64/R/library/optimx/help/optimx.rdx
/usr/lib64/R/library/optimx/help/paths.rds
/usr/lib64/R/library/optimx/html/00Index.html
/usr/lib64/R/library/optimx/html/R.css
/usr/lib64/R/library/optimx/unitTests/runit.1.R
/usr/lib64/R/library/optimx/unitTests/runit.all.R
