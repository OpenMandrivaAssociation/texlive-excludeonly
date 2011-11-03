# revision 17262
# category Package
# catalog-ctan /macros/latex/contrib/excludeonly
# catalog-date 2010-03-01 08:47:36 +0100
# catalog-license pd
# catalog-version 1.0
Name:		texlive-excludeonly
Version:	1.0
Release:	1
Summary:	Prevent files being \include-ed
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/excludeonly
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/excludeonly.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/excludeonly.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines an \excludeonly command, which is (in
effect) the opposite of \includeonly. If both \includeonly and
\excludeonly exist in a document, only files "allowed" by both
will be included. The package redefines the internal \@include
command, so it conflicts with packages that do the same.
Examples are the classes paper.cls and thesis.cls.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/excludeonly/excludeonly.sty
%doc %{_texmfdistdir}/doc/latex/excludeonly/excludeonly.pdf
%doc %{_texmfdistdir}/doc/latex/excludeonly/excludeonly.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
