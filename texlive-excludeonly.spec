%global tl_name excludeonly
%global tl_revision 17262

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Prevent files being \include-ed
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/excludeonly
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/excludeonly.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/excludeonly.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines an \excludeonly command, which is (in effect) the
opposite of \includeonly. If both \includeonly and \excludeonly exist in
a document, only files "allowed" by both will be included. The package
redefines the internal \@include command, so it conflicts with packages
that do the same. Examples are the classes paper.cls and thesis.cls.

