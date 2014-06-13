# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hitec
# catalog-date 2008-11-07 01:12:48 +0100
# catalog-license lppl
# catalog-version 0.0(beta)
Name:		texlive-hitec
Version:	0.0beta
Release:	7
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.0beta-2
+ Revision: 752582
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.0beta-1
+ Revision: 718621
- texlive-hitec
- texlive-hitec
- texlive-hitec
- texlive-hitec

