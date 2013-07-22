%global packname scales
%global rlibdir %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.2.3
Release:          1
Summary:          Scale functions for graphics
Group:            Sciences/Mathematics
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-methods R-RColorBrewer R-stringr R-dichromat 
Requires:         R-munsell >= 0.2 R-plyr >= 1.2 R-labeling R-testthat
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-RColorBrewer R-stringr R-dichromat 
BuildRequires:    R-munsell >= 0.2 R-plyr >= 1.2 R-labeling R-testthat

%description
Scales map data to aesthetics, and provide methods for
automatically determining breaks and labels for axes and legends.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tests
