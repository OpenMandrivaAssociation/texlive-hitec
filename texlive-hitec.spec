Name:		texlive-hitec
Version:	15878
Release:	2
Summary:	Class for documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hitec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitec.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An article-based class designed for use for documentation in
high-technology companies.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hitec/hitec.cls
%doc %{_texmfdistdir}/doc/latex/hitec/README
%doc %{_texmfdistdir}/doc/latex/hitec/hitec_doc.pdf
%doc %{_texmfdistdir}/doc/latex/hitec/hitec_doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
