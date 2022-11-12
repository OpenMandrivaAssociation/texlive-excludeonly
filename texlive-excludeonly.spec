Name:		texlive-excludeonly
Version:	17262
Release:	1
Summary:	Prevent files being \include-ed
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/excludeonly
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/excludeonly.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/excludeonly.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines an \excludeonly command, which is (in
effect) the opposite of \includeonly. If both \includeonly and
\excludeonly exist in a document, only files "allowed" by both
will be included. The package redefines the internal \@include
command, so it conflicts with packages that do the same.
Examples are the classes paper.cls and thesis.cls.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/excludeonly/excludeonly.sty
%doc %{_texmfdistdir}/doc/latex/excludeonly/excludeonly.pdf
%doc %{_texmfdistdir}/doc/latex/excludeonly/excludeonly.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
