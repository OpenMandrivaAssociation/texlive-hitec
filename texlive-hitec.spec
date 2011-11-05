# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hitec
# catalog-date 2008-11-07 01:12:48 +0100
# catalog-license lppl
# catalog-version 0.0(beta)
Name:		texlive-hitec
Version:	0.0beta
Release:	1
Summary:	Class for documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hitec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitec.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An article-based class designed for use for documentation in
high-technology companies.

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
%{_texmfdistdir}/tex/latex/hitec/hitec.cls
%doc %{_texmfdistdir}/doc/latex/hitec/README
%doc %{_texmfdistdir}/doc/latex/hitec/hitec_doc.pdf
%doc %{_texmfdistdir}/doc/latex/hitec/hitec_doc.tex
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
