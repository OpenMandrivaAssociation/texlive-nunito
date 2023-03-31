Name:		texlive-nunito
Version:	57429
Release:	2
Summary:	The Nunito font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nunito
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nunito.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nunito.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX and pdfLaTeX support for the Nunito
family of fonts, designed by Vernon Adams, Cyreal.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/nunito
%{_texmfdistdir}/fonts/vf/public/nunito
%{_texmfdistdir}/fonts/type1/public/nunito
%{_texmfdistdir}/fonts/tfm/public/nunito
%{_texmfdistdir}/fonts/opentype/public/nunito
%{_texmfdistdir}/fonts/map/dvips/nunito
%{_texmfdistdir}/fonts/enc/dvips/nunito
%doc %{_texmfdistdir}/doc/fonts/nunito

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
