Name:		texlive-minorrevision
Version:	32165
Release:	2
Summary:	Quote and refer to a manuscript for minor revisions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minorrevision
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minorrevision.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minorrevision.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports those who publish articles in peer-
reviewed journals. In the final stages of the review process,
the authors typically have to provide an additional document
(such as a letter to the editors), in which they provide a list
of modifications that they made to the manuscript. The package
automatically provides line numbers and quotations from the
manuscript, for this letter. The package loads the package
lineno, so (in effect) shares lineno's incompatibilities.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/minorrevision/minorrevision.sty
%doc %{_texmfdistdir}/doc/latex/minorrevision/README
%doc %{_texmfdistdir}/doc/latex/minorrevision/minorrevision.pdf
%doc %{_texmfdistdir}/doc/latex/minorrevision/minorrevision.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
