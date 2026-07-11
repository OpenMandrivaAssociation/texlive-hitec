%global tl_name hitec
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0beta
Release:	%{tl_revision}.1
Summary:	Class for documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hitec
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitec.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An article-based class designed for use for documentation in high-
technology companies.

