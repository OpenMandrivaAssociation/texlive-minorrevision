%global tl_name minorrevision
%global tl_revision 32165

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Quote and refer to a manuscript for minor revisions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minorrevision
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minorrevision.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minorrevision.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports those who publish articles in peer-reviewed
journals. In the final stages of the review process, the authors
typically have to provide an additional document (such as a letter to
the editors), in which they provide a list of modifications that they
made to the manuscript. The package automatically provides line numbers
and quotations from the manuscript, for this letter. The package loads
the package lineno, so (in effect) shares lineno's incompatibilities.

