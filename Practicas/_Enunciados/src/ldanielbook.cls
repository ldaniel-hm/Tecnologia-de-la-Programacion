%%%%%%%%%%%%%%%%%%%%%%
%% start of file `ldanielbook.cls'.
%% Copyright 2021 ldaniel@um.es 
%%
%% available at https://github.com/ldanielbook
% 
%%%%%%%%%%%%%%%%%%%%%
% % !Mode:: "TeX:UTF-8"
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ldanielbook}[2021/04/12 v0.1 ldaniel document class]


\RequirePackage{kvoptions}  % to use options in key-value format for their package options.
\RequirePackage{etoolbox} % Es usado por el paquete noindentafter, por eso se comenta
\SetupKeyvalOptions{family=LDANIEL, prefix=LDANIEL@, setkeys=\kvsetkeys}
\newcommand{\ekv}[1]{\kvsetkeys{LDANIEL}{#1}}


% --- Idioma
\DeclareStringOption[es]{lang}

\DeclareVoidOption{en}{\ekv{lang=en}}
\DeclareVoidOption{es}{\ekv{lang=es}}

% --- Fuente
\DeclareStringOption[newtxtext]{font}

\DeclareVoidOption{newtxtext}{\ekv{font=newtxtext}}
\DeclareVoidOption{mathptmx}{\ekv{font=mathptmx}}
\DeclareVoidOption{times}{\ekv{font=times}}
\DeclareVoidOption{timesroman}{\ekv{font=timesroman}}
\DeclareVoidOption{helvet}{\ekv{font=helvet}}
\DeclareVoidOption{lmodern}{\ekv{font=lmodern}}
\DeclareVoidOption{ckurier}{\ekv{font=ckurier}}
\DeclareVoidOption{lkurier}{\ekv{font=lkurier}}
\DeclareVoidOption{canttor}{\ekv{font=canttor}}
\DeclareVoidOption{lanttor}{\ekv{font=lanttor}}
\DeclareVoidOption{iwona}{\ekv{font=iwona}}
\DeclareVoidOption{ciwona}{\ekv{font=ciwona}}
\DeclareVoidOption{cmbright}{\ekv{font=cmbright}}
\DeclareVoidOption{avant}{\ekv{font=avant}}
\DeclareVoidOption{anttor}{\ekv{font=anttor}}
\DeclareVoidOption{libris}{\ekv{font=libris}}
\DeclareVoidOption{palatino}{\ekv{font=palatino}}

% --- Subrayados
%\DeclareStringOption[ulem]{underline}
%
%\DeclareVoidOption{ulem}{\ekv{underline=ulem}}
%\DeclareVoidOption{soul}{\ekv{underline=soul}}

% --- Índices parciales
\DeclareStringOption[etoc]{minitoc}

\DeclareVoidOption{mintoc}{\ekv{minitoc=mintoc}}
\DeclareVoidOption{etoc}{\ekv{minitoc=etoc}}

% --- Geometría
\DeclareStringOption[normal]{geometry}

\DeclareVoidOption{apa}{\ekv{geometry=apa}}
\DeclareVoidOption{normal}{\ekv{geometry=normal}}
\DeclareVoidOption{pad}{\ekv{geometry=pad}}

% --- Espacio entre líneas
\DeclareStringOption[one]{space}

\DeclareVoidOption{none}{\ekv{space=none}}
\DeclareVoidOption{half}{\ekv{space=half}}
\DeclareVoidOption{one}{\ekv{space=one}}
\DeclareVoidOption{onehalf}{\ekv{space=onehalf}}
\DeclareVoidOption{double}{\ekv{space=double}}


% --- Indentanción
\DeclareStringOption[indentnormal]{indent}
\DeclareVoidOption{indentnormal}{\ekv{indent=indentnormal}}
\DeclareVoidOption{noindent}{\ekv{indent=noindent}}

% --- Color
\DeclareStringOption[blue]{color}
\DeclareVoidOption{green}{\ekv{color=green}}
\DeclareVoidOption{cyan}{\ekv{color=cyan}}
\DeclareVoidOption{blue}{\ekv{color=blue}}
\DeclareVoidOption{gray}{\ekv{color=gray}}
\DeclareVoidOption{black}{\ekv{color=black}}
\DeclareVoidOption{nocolor}{\ekv{color=none}}


% --- Índices parciales
\DeclareStringOption[titlesec]{pagestyle}

\DeclareVoidOption{fancy}{\ekv{pagestyle=fancyhdr}}
\DeclareVoidOption{titlesec}{\ekv{pagestyle=titlesec}}




% --------------------------------------------------------------------------------------------------------------------------
% An ex­tended ver­sion of TEX (which is ca­pa­ble of run­ning as if it were TEX un­mod­i­fied.
% Está ralacionado con el kernel de TeX. Se supone que etex se carga por defecto, pero parece que no siempre.
% --------------------------------------------------------------------------------------------------------------------------
\RequirePackage{etex} 
\reserveinserts{28}

% --------------------------------------------------------------------------------------------------------------------------
% --- BOOK
% --------------------------------------------------------------------------------------------------------------------------

% ----- Default Options -----
\DeclareDefaultOption{\PassOptionsToClass{\CurrentOption}{book}}

\ProcessKeyvalOptions*\relax
% \ProcessOptions*\relax
%\LoadClass[a4paper,oneside]{book}
\LoadClass{book}



% --------------------------------------------------------------------------------------------------------------------------
% --- Idioma
% --------------------------------------------------------------------------------------------------------------------------

\ifdefstring{\LDANIEL@lang}{en}{
	\renewcommand{\chaptername}{Chapter \thechapter}
	\newcommand{\authorname}{\textbf{Author: }}
}{\relax}

\ifdefstring{\LDANIEL@lang}{es}{
	\RequirePackage[spanish]{babel}     % Lenguaje para hyphenation http://www.texnia.com/spanishopt.html
	\selectlanguage{spanish} 
	\addto\captionsspanish{\renewcommand{\chaptername}{Tema}}
	\addto\captionsspanish{\renewcommand{\tablename}{Tabla}}
	
	% Si se usa minitoc
	\newcommand{\mtctitlename}{Contenido del tema}
    % Si se usa etoc
    \newcommand{\etocstyle}{\subsubsection*{Índice del Capítulo}}
    %
    \newcommand{\notename}{Nota}
	
	%\usepackage[autostyle, spanish = spanish]{csquotes}% manejo de comillas: " "
    %\MakeOuterQuote{"}
    \decimalpoint  % El punto decimal es un punto, y no una coma.
    
	% --- Codificación del texto
	\hyphenpenalty=10000 \exhyphenpenalty=10000 \pretolerance=10000 % No rompe palabras
	% Si inputenc se usa con xelatex dará este mensaje de error
	% Package inputenc Warning: inputenc package ignored with utf8 based engines.
	% porque inputenc se caraga "despues".....
	% ... https://tex.stackexchange.com/questions/282678/why-does-inputenc-abandon-so-quickly-under-utf8-based-engines
	%\RequirePackage[utf8]{inputenc}   % Para reconocer los acentos castellano. Se puede usar á en vez de \'{a}

	
	% --- Apariencia del texto normal: acentos
	%	Si diera problema con alguna fuente, ponerlo después del paquete correspondiente.
	\RequirePackage[T1]{fontenc}       % his is font encoding (determines what kind of font is used), not input encoding.
	
	% Symbol euro
	\RequirePackage{eurosym}
}{\relax}


% Pro­vides var­i­ous dif­fer­ent for­mats for the text cre­ated by the com­mand \to­day
% Permite format 12h o 24h
% the datetime package is now compatible with babel, however you must load the datetime package after the babel package.
\RequirePackage{datetime}

% --------------------------------------------------------------------------------------------------------------------------
% --- Hyperref
% --------------------------------------------------------------------------------------------------------------------------
\usepackage{url}

\usepackage[final]{hyperref}
\hypersetup{
	breaklinks,
	colorlinks=true,       % false: boxed links; true: colored links
%	bookmarks=true,         % show bookmarks bar?
    unicode=true          % non-Latin characters in Acrobat’s bookmarks
%    pdftoolbar=false,        % show Acrobat’s toolbar?
%    pdfmenubar=true,        % show Acrobat’s menu?
%    pdffitwindow=false,     % window fit to page when opened
%    pdfstartview={FitH},    % fits the width of the page to the window
%    pdfnewwindow=true,      % links in new window
	pdfkeywords={ldanielBook},
%    linktocpage,
%    colorlinks=true,       % false: boxed links; true: colored links
    linkcolor=red!70!black,          % color of internal links (change box color with linkbordercolor)
%    citecolor=green,        % color of links to bibliography
%    filecolor=magenta,      % color of file links
    urlcolor=blue!60!black           % color of external links
}

% --------------------------------------------------------------------------------------------------------------------------
% --- GEOMETRIA
% --------------------------------------------------------------------------------------------------------------------------
\RequirePackage{geometry}

% https://normasapa.com/margenes-normas-apa/
% use the left and right keys, because they are actually synonyms for  inner and outer in twoside mode
% In case you want to disable the swapping of margins on alternate pages, add the asymmetric option.
% So far you've used the twoside option in your document class, but you want to do without this option? 
% Well, use the twoside option of geometry instead.
\ifdefstring{\LDANIEL@geometry}{apa}{
	\geometry{
		a4paper,
		twoside,
		top=2.5cm, 
		bottom=2.5cm, 
		left=2.5cm, 
		right=1.2cm, 
		headsep=20pt 
	}
}{\relax}


\ifdefstring{\LDANIEL@geometry}{normal}{
	\geometry{
		a4paper,
		top=25.4mm, 
		bottom=25.4mm,
		%headheight=2.17cm,
		%headsep=4mm,
		%footskip=12mm
		left=2cm, 
		right=2cm, 
		headsep=20pt
	}
	\ifdefstring{\LDANIEL@geometry}{margintrue}{
		\geometry{
			marginparwidth=5cm, 
			marginparsep=5mm,
			left=2cm,
			right=7cm
		}
	}{\relax}
}{\relax}

\ifdefstring{\LDANIEL@geometry}{pad}{
	\geometry{
		paperwidth=7.5in, 
		paperheight=10in,
		margin=16mm,
		headheight=2.17cm,
		footskip=4mm
}}{\relax}



% --------------------------------------------------------------------------------------------------------------------------
% --- Espacio entre líneas
% --------------------------------------------------------------------------------------------------------------------------
%
\RequirePackage{setspace}
%\begin{doublespace} % onehalfspacing, singlespacing 
%...
%\end{doublespace} % onehalfspacing, singlespacing 
%
%\begin{spacing}{2.0}
%...
%\end{spacing}

\ifdefstring{\LDANIEL@space}{none}{
	\setstretch{0.0}
	%\setlength{\parskip}{0.0\baselineskip}
}{\relax}

\ifdefstring{\LDANIEL@space}{half}{
	\setstretch{0.5}
	%\setlength{\parskip}{.25\baselineskip}
}{\relax}

\ifdefstring{\LDANIEL@space}{one}{
	\singlespacing
}{\relax}

\ifdefstring{\LDANIEL@space}{onehalf}{
	\onehalfspacing
}{\relax}

\ifdefstring{\LDANIEL@space}{double}{
	\doublespacing
}{\relax}

% OTRA FORMA
%% For double-spacing you have to use 1.6 and for one-and-a-half spacing 1.3"
%\linespread{1.1}


% --------------------------------------------------------------------------------------------------------------------------
% --- Indentancion
% --------------------------------------------------------------------------------------------------------------------------
%
% to automatically suppress indentations in following paragraphs, 
% specifically those following a particular macro or environment.
% El siguiente parquete lo requiere etoolbox, así que se comenta
%\RequirePackage{noindentafter}  % https://ctan.org/pkg/noindentafter

\ifdefstring{\LDANIEL@indent}{indentnormal}{
 % NONE
}{\relax}

\ifdefstring{\LDANIEL@indent}{noindent}{
	\setlength\parindent{0.0cm}
}{\relax}



% --------------------------------------------------------------------------------------------------------------------------
% --- Fonts
% --------------------------------------------------------------------------------------------------------------------------
%
% APA 6 es Times New Roman, que no está en LaTeX.
% Una opción. URW Nimbus Roman http://www.tug.dk/FontCatalogue/urwnimbusroman/  Nimbus Roman es una versión GNU
\ifdefstring{\LDANIEL@font}{mathptmx}{
	\RequirePackage{mathptmx} % This pack­age de­fines Adobe Times Ro­man (or equiv­a­lent) as de­fault text font, and pro­vides maths sup­port us­ing glyphs
}{\relax}


\ifdefstring{\LDANIEL@font}{newtxtext}{
	\RequirePackage{newtxtext}
	%\RequirePackage{newtxmath}
}{\relax}


\ifdefstring{\LDANIEL@font}{times}{
	\RequirePackage{times} 
}{\relax}

\ifdefstring{\LDANIEL@font}{timesroman}{
	\RequirePackage{newtxtext}   % Times Roman
}{\relax}

\ifdefstring{\LDANIEL@font}{helvet}{
	\RequirePackage[scaled=0.86]{helvet}  % Helvetica
}{\relax}

%\RequirePackage{pslatex}          % Fuentes finas postscript
\ifdefstring{\LDANIEL@font}{lmodern}{
	\RequirePackage{lmodern} 
}{\relax}

\ifdefstring{\LDANIEL@font}{ckurier}{
	\RequirePackage[condensed,math]{kurier} 
}{\relax}

\ifdefstring{\LDANIEL@font}{lkurier}{
	\RequirePackage[light,math]{kurier}%http://www.tug.dk/FontCatalogue/
}{\relax}

\ifdefstring{\LDANIEL@font}{canttor}{
	\RequirePackage[condensed,math]{anttor} 
}{\relax}

\ifdefstring{\LDANIEL@font}{lanttor}{
	\RequirePackage[light,condensed,math]{anttor} 
}{\relax}

\ifdefstring{\LDANIEL@font}{iwona}{
	\RequirePackage[math]{iwona} 
}{\relax}

\ifdefstring{\LDANIEL@font}{ciwona}{
	\RequirePackage[condensed,math]{iwona}
}{\relax}

\ifdefstring{\LDANIEL@font}{cmbright}{
	\RequirePackage{cmbright} 
}{\relax}

\ifdefstring{\LDANIEL@font}{avant}{
	\RequirePackage{avant} 
}{\relax}

\ifdefstring{\LDANIEL@font}{anttor}{
	\RequirePackage[math]{anttor}  % http://www.tug.dk/FontCatalogue/antykwatorunska/
}{\relax}

\ifdefstring{\LDANIEL@font}{libris}{
	\RequirePackage{pslatex}
	\RequirePackage{libris}  % http://www.tug.dk/FontCatalogue/librisadf/
}{\relax}

\ifdefstring{\LDANIEL@font}{palatino}{
	\RequirePackage{palatino}
	\linespread{1.05}                 % Fuente Palatino necesita espaciado
	%The Pazo Math fonts are a family of PostScript fonts suitable 
	% for typesetting mathematics in combination with the Palatino family of text fonts.
	\RequirePackage[sc]{mathpazo}    % Fuentes mathpazo
}{\relax}


% --------------------------------------------------------------------------------------------------------------------------
% --- Fuente particular
%	Para usar una fuente en particular usar los siguientes comandos:
% 	Ejemplo: 
%\newcommand*{\myfont}{\fontfamily{kurier}\selectfont}
\newcommand*{\myfont}{\fontfamily{lmr}\selectfont}
\newcommand*{\myfontEjemplo}{\fontfamily{kurier}\selectfont}
\newcommand*{\action}{\fontfamily{pag}\selectfont}
% --------------------------------------------------------------------------------------------------------------------------

% \newcommand*{\myfont}{\fontfamily{<familyname>}\selectfont}
% \newenvironment{myfont}{\fontfamily{<familyname>}\selectfont}{\par}
% \newcommand*{\myfont}{\fontfamily{fvs}\selectfont}
%Family                 Font Name
%pag                    Avant Garde
%fvs                    Bitstream Vera Sans
%pbk                    Bookman
%bch                    Charter
%ccr                    Computer Concrete
%cmr                    Computer Modern
%pcr                    Courier
%mdugm                  Garamond
%phv                    Helvetica
%fi4                    Inconsolata
%lmr                    Latin Modern
%lmss                   Latin Modern Sans
%lmtt                   Latin Modern Typewriter
%LinuxBiolinumT-OsF     Linux Biolinum (formerly 'fxb' in older package versions)
%LinuxLibertineT-OsF    Linux Libertine (formerly 'fxl' in older package versions)
%pnc                    New Century Schoolbook
%ppl                    Palatino
%ptm                    Times
%uncl                   Uncial
%put                    Utopia
%pzc                    Zapf Chancery


% --------------------------------------------------------------------------------------------------------------------------
% --- Fuentes y entornos matemáticos 
% --------------------------------------------------------------------------------------------------------------------------


% AMS-Math
\RequirePackage{amsmath}
\RequirePackage{mathtools} % https://ctan.org/pkg/mathtools.  based on ams­math,  fixes various deficiencies of amsmath
 					% Math­tools is part of the mh bun­dle
					% to en­hance the ap­pear­ance of doc­u­ments con­tain­ing a lot of math­e­mat­ics. 
					
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{amsthm} % Permite usar distintos entornos de teoremas 
%%\theoremstyle{plain}   % plain es uno de los estilos de apariencia.
% Se puede definir un estilo propio con \newtheoremstyle. Por ejemplo.
% ------------------------------------------------------------
%\newtheoremstyle{color}% ⟨name⟩
%{3pt}%
%{3pt}%
%{}%
%{}%
%{}%
%{}%
%{.5em}%
%{\colorbox{lightgray}{\textcolor{white}{#1 #2.}}}%
%\theoremstyle{color}
%
%\newtheorem{ejercicio}{\sc Ejercicio }
%
% Para más detalles, la guía rápida: https://en.wikibooks.org/wiki/LaTeX/Theorems


\usepackage{thmtools} %%  https://osl.ugr.es/CTAN/macros/latex/contrib/thmtools/doc/thmtools-manual.pdf
\declaretheoremstyle[
	spaceabove=6pt, 
	spacebelow=6pt,
	notefont=\bfseries, %\mdseries, 
	%notebraces={(}{)},
	bodyfont=\normalfont,
	qed=\qedsymbol
]{mystyle}

\declaretheoremstyle[
	spaceabove=6pt, 
	spacebelow=6pt,
	notefont=\bfseries, %\mdseries, 
	%notebraces={(}{)},
	bodyfont=\normalfont
]{ejerciciostyle}

\declaretheoremstyle[
	spaceabove=6pt, 
	spacebelow=6pt,
	notefont=\bfseries%, %\mdseries, 
	%notebraces={(}{)},
	% bodyfont=\normalfont,
	%headfont=\normalfont\bfseries
]{stylebox}

%\declaretheorem[style=ejerciciostyle, numberwithin=chapter]{ejercicio}
\declaretheorem[style=mystyle, numberwithin=chapter]{ejemplo}
%\declaretheorem[style=mystyle, numberwithin=chapter]{definicion}
%\declaretheorem[style=stylebox,  mdframed={linecolor=white, skipabove = 6pt}, thmbox={style=M, hskip=-0.1em}]{TDA}
%\declaretheorem[style=stylebox,  thmbox={style=M, hskip=0.4em, leftmargin=0.4em}]{TDA}

%\usepackage[hskip=-0.1em]{thmbox}
%\newtheorem[M]{TDA}{TDA}




% --------------------------------------------------------------------------------------------------------------------------
% --- Otras fuentes y símbolos.
% --------------------------------------------------------------------------------------------------------------------------

%% Al final parecer que necesito los dos.
%\ifdefstring{\LDANIEL@underline}{ulem}{
	\RequirePackage{ulem} 	% https://ctan.javinator9889.com/macros/latex/contrib/ulem/ulem.pdf
							% \uline{important} underlined text like important
							% \uuline{urgent} double-underlined text like urgent
							% \uwave{boat} wavy underline like boat
							% \sout{wrong} line struck through word like wrong
							% \xout{removed} marked over like //////////
							% \dashuline{dashing} dashed underline like dashing
							% \dotuline{dotty} dotted underline like ......
%}{\relax}
%\ifdefstring{\LDANIEL@underline}{soul}{
	% Provides hyphenatable spacing out (letterspacing), underlining, striking out, etc., 
	% \RequirePackage{soul}
	% This package extends package soul and adds some support for UTF-8
	\RequirePackage{soul}       % \textst{texto}, tacha el texto.
%}{\relax}

\RequirePackage{menukeys} % It contains symbols for all Apple and Windows Keys.

\RequirePackage[tikz]{bclogo}     % Creating colourful boxes with logos
\RequirePackage{textcomp}	% Acentos, monedas,copyright y otros, En modo texto: flechas, 
							%	delimitadores, símbolos matemáticos, y otros.						
\RequirePackage{bbding}	% Flechas, tijeras, lápices, plumas, manos, cruces, marcas Xs, 
							% 	estrellas, flores y similares, figuras geométricas, 
\RequirePackage{pifont}		% Símbolos dings (principalmente para listas)
\RequirePackage{wasysym}	% De lo más completos
%\RequirePackage{marvosym}           % DEBE SER CARGADO DESPUES DE `ams' porque Redefine \Rightarrow
%\RequirePackage[clock]{ifsym}	% Algunos permiten argumentos como clock

\renewenvironment{dinglist}[2][red] % Color por defecto
{\begin{list}{\color{#1} \ding{#2}}{}}{\end{list}}
 \newcommand{\SimboloA}{43}          % Posibles s�mbolos a utilizar
\newcommand{\SimboloB}{243}         % Se usa as�:
\newcommand{\SimboloC}{224}         % \begin{dinglist}[COLOR]{\SimboloC}
\newcommand{\SimboloD}{219}         %   \item ... \item ...
\newcommand{\SimboloE}{242}         % \end{dinglist}
 
 


% --------------------------------------------------------------------------------------------------------------------------
% --- Colores
% --------------------------------------------------------------------------------------------------------------------------
%\RequirePackage{colortbl}
%\RequirePackage[dvipsnames]{xcolor}
\RequirePackage{xcolor}
\ifdefstring{\LDANIEL@color}{green}{
  \definecolor{structurecolor}{RGB}{0,120,2}%
  \definecolor{main}{RGB}{0,120,2}%
  \definecolor{second}{RGB}{230,90,7}%
  \definecolor{third}{RGB}{0,160,152}%
}{\relax}
\ifdefstring{\LDANIEL@color}{cyan}{
  \definecolor{structurecolor}{RGB}{31,186,190}%
  \definecolor{main}{RGB}{59,180,5}%
  \definecolor{second}{RGB}{175,153,8}%
  \definecolor{third}{RGB}{244,105,102}%
}{\relax}
\ifdefstring{\LDANIEL@color}{blue}{
  \definecolor{structurecolor}{RGB}{60,113,183}
  \definecolor{main}{RGB}{0,166,82}%
  \definecolor{second}{RGB}{255,134,24}%
  \definecolor{third}{RGB}{0,174,247}%
}{\relax}
\ifdefstring{\LDANIEL@color}{gray}{
  \definecolor{structurecolor}{RGB}{150,150,150}
  \definecolor{main}{RGB}{150,150,150}%
  \definecolor{second}{RGB}{150,150,150}%
  \definecolor{third}{RGB}{150,150,150}%
}{\relax}
\ifdefstring{\LDANIEL@color}{black}{
  \definecolor{structurecolor}{RGB}{0,0,0}
  \definecolor{main}{RGB}{0,0,0}%
  \definecolor{second}{RGB}{0,0,0}%
  \definecolor{third}{RGB}{0,0,0}%
}{\relax}





% --------------------------------------------------------------------------------------------------------------------------
% --- Entornos para la inclusión/creación de gráficos
% --------------------------------------------------------------------------------------------------------------------------
%\RequirePackage{graphicx}  mdframed loads graphicx you don't need to load graphicx (and that's the cause of the clash initially)

\RequirePackage{wrapfig}

% --- Tikz
\usepackage{tikz}
\usetikzlibrary{arrows,shapes.geometric,topaths,patterns,snakes,automata,shadows, positioning, matrix}%,backgrounds,arrows,,}

% --- graphviz
%\usepackage[pdf]{graphviz}
%\usepackage{morewrites}  % Es imprescindible para que funciones graphviz
%%   \digraph{abc}{
%%      rankdir=LR;
%%      a -> b -> c;
%%   }

% --- dot2texi
%\usepackage[autosize]{dot2texi}
% Ejemplo para dot2tex
%\begin{dot2tex}[neato,mathmode]
%digraph G {
%node [shape="circle"];
%a_1 -> a_2 -> a_3 -> a_4 -> a_1;
%}
%\end{dot2tex}




% --------------------------------------------------------------------------------------------------------------------------
% --- Entornos para mejorar las listas
% --------------------------------------------------------------------------------------------------------------------------
\RequirePackage[inline]{enumitem} % https://osl.ugr.es/CTAN/macros/latex/contrib/enumitem/enumitem.pdf
%\begin{enumerate}[nosep]
%\setlist{nosep} % or 
%\setlist{noitemsep} % to leave space around whole list
\setlist{itemsep=0.0\baselineskip, parsep=0.1\baselineskip, topsep=0.2\baselineskip} % noitemsep

% --------------------------------------------------------------------------------------------------------------------------
% --- Entornos para mejorar las tablas
% --------------------------------------------------------------------------------------------------------------------------
\RequirePackage{multicol}
\RequirePackage{multirow}
\RequirePackage{tabularx}
\RequirePackage{hhline}

% --------------------------------------------------------------------------------------------------------------------------
% --- Mejora general de entornos
% --------------------------------------------------------------------------------------------------------------------------
%\usepackage{subfigure}
\RequirePackage{subcaption} % http://ctan.org/pkg/{caption,subcaption}
\RequirePackage{float}  % https://ctan.org/pkg/float. Im­proves the in­ter­face for defin­ing float­ing ob­jects such as fig­ures and ta­bles

%----------------------------------------------------------------------------------------
%	Customize toc/lof/lot \localtableofcontents
%
% https://texblog.org/2011/09/09/10-ways-to-customize-tocloflot/
%----------------------------------------------------------------------------------------
\ifdefstring{\LDANIEL@minitoc}{mintoc}{
	\RequirePackage{minitoc}
	\renewcommand{\mtctitle}{\mtctitlename}
	\setcounter{minitocdepth}{1}    % Show until sections in minitoc
	\setcounter{minitocdepth}{3}    % Show until subsubsections in minitoc
}{\relax}

\ifdefstring{\LDANIEL@minitoc}{etoc}{
	\RequirePackage{etoc} % Usar \localtableofcontents al inicio del capítulo
	\etocsetnexttocdepth{3}
	\etocsettocstyle{\etocstyle}{}
}{\relax}

%\usepackage{titletoc}


%----------------------------------------------------------------------------------------
%	Encabezados de página
%----------------------------------------------------------------------------------------

\ifdefstring{\LDANIEL@pagestyle}{fancyhdr}{
	\RequirePackage{fancyhdr} %Necesario para la cabecera y el pie de página de configuración

	\pagestyle{fancy}
	\renewcommand{\chaptermark}[1]{\markboth{\sffamily\normalsize\bfseries #1}{}} % Fuente capítulo
	% Texto en secciones
	\renewcommand{\sectionmark}[1]{\markright{\sffamily\normalsize\thesection\hspace{5pt}#1}{}} 
	% Configuración de fuentes para el número de página en el encabezado


	% https://normasapa.com/formato-apa-presentacion-trabajos-escritos/
	% La enumeración de las paginas deben estar ubicadas en las equinas superiores.
	\fancyhf{} 
	\fancyhead[LE]{\sffamily\normalsize\bfseries\thepage \hspace{10pt} \textrm \leftmark} 
	\fancyhead[RO]{\rightmark \hspace{10pt} \sffamily\normalsize\bfseries\thepage} 


	%\fancyhead[LE,RO]{\sffamily\normalsize\thepage} 
	%\fancyhead[LO]{\rightmark} %
	%\fancyhead[RE]{\leftmark} % 

	\renewcommand{\headrulewidth}{0.5pt} % Ancho de la norma bajo el encabezado
	\addtolength{\headheight}{2.5pt} % Aumente el espacio alrededor de la cabecera 
	\renewcommand{\footrulewidth}{0pt} % Elimina la línea en el pie de página

	% Estilo para cuando se especifica "pagestyle plain"
	\fancypagestyle{plain}{\fancyhead{}\renewcommand{\headrulewidth}{0pt}} 

	% Elimina el encabezado de las páginas impares vacías al final de los capítulos
	\makeatletter
	\renewcommand{\cleardoublepage}{
	\clearpage\ifodd\c@page\else
	\hbox{}
	\vspace*{\fill}
	\thispagestyle{empty}
	\newpage
	\fi}
}{\relax}



\ifdefstring{\LDANIEL@pagestyle}{titlesec}{
	\usepackage[pagestyles]{titlesec}
}{\relax}



%
%% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
%% LISTADOS
%% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
\usepackage{listings}

% some listings shenanigans to have access to the current listings style
% within an escape to LaTeX
\makeatletter
\newcommand\currentStyle@lstparam{}
\lst@AddToHook{Output}{\global\let\currentStyle@lstparam\lst@thestyle}
\lst@AddToHook{OutputOther}{\global\let\currentStyle@lstparam\lst@thestyle}
\newcommand\listparam{\currentStyle@lstparam ns} %<-- try to change that to `xs'
\makeatother

%% Los listings precisan parámetros especiales, si no puede fallar la generación del PDF %%
\lstset{
 extendedchars=true, 
 inputencoding=utf8,
 literate={á}{{\'a}}1
 {é}{{\'e}}1
 {í}{{\'i}}1
 {ó}{{\'o}}1
 {ú}{{\'u}}1
 {ñ}{{\~n}}1
 {¿}{{?`}}1
 {¡}{{!`}}1
 {"}{{"}}1
}

\lstset{
 numbers=left,
 frame=leftline, 
 numbersep=1pt, 
 numberstyle=\tiny\color{red}
}



            \newcounter{countCode}
            \lstnewenvironment{code} [1][caption=Ponme caption, label=default]{%
                \renewcommand*{\lstlistingname}{Programa} 
                \setcounter{lstlisting}{\value{countCode}} 
                \lstset{ %
                language=java,
                basicstyle=\ttfamily\footnotesize,       % the size of the fonts that are used for the code
                numbers=left,                   % where to put the line-numbers
                numberstyle=\sc,      % the size of the fonts that are used for the line-numbers
                stepnumber=1,                   % the step between two line-numbers. 
                numbersep=5pt,                 % how far the line-numbers are from the code
                numberstyle=\color{red!50!blue},
                    backgroundcolor=\color{lightgray!20},
                rulecolor=\color{blue},
                keywordstyle=\color{red}\bfseries,
                commentstyle = \color{green!50!blue},
                showspaces=false,               % show spaces adding particular underscores
                showstringspaces=false,         % underline spaces within strings
                showtabs=false,                 % show tabs within strings adding particular underscores
                frame=single,                   % adds a frame around the code
                framexleftmargin=0mm,
                numberblanklines=false,
                xleftmargin=5pt,
                breaklines=true,
                breakatwhitespace=true,
                breakautoindent=true,
                captionpos=t,
                texcl=true,
                tabsize=2,                      % sets default tabsize to 3 spaces
                extendedchars=true,
                inputencoding=utf8, 
                escapechar=\%,
                morekeywords={print, println, size, background, strokeWeight, fill, line, rect, ellipse, triangle, arc, save, PI, HALF_PI, QUARTER_PI, TAU, TWO_PI, width, height,String,},
                emph=[1]{print,println,}, emphstyle=[1]{\color{blue}}, % Mis palabras clave.
                emph=[2]{width,height,}, emphstyle=[2]{\bf\color{violet}}, % Mis palabras clave.
                emph=[3]{PI, HALF_PI, QUARTER_PI, TAU, TWO_PI}, emphstyle=[3]\color{orange!50!violet}, % Mis palabras clave.
                emph=[4]{line, rect, ellipse, triangle, arc,}, emphstyle=[4]\color{green!70!black}, % Mis palabras clave.
                emph=[4]{String,}, emphstyle=[4]\color{red!70!blue}, % Mis palabras clave.
                %emph=[5]{size, background, strokeWeight, fill,}, emphstyle=[5]{\tt \color{red!30!blue}}, % Mis palabras clave.
                %emph={[2]sqrt,baset}, emphstyle={[2]\color{blue}}, % f(sqrt(2)), sqrt a nivel 2 se pondrá azul
                #1}}{\addtocounter{countCode}{1}}



            \newcounter{countOut}
            \lstnewenvironment{out} [1][caption=Ponme caption, label=default]{%
                \renewcommand*{\lstlistingname}{Consola}  
                \setcounter{lstlisting}{\value{countOut}} 
                \lstset{ %
                language=bash,
                basicstyle=\ttfamily\footnotesize\color{white},       % the size of the fonts that are used for the code
                numbers=left,                   % where to put the line-numbers
                numberstyle=\sc,      % the size of the fonts that are used for the line-numbers
                stepnumber=1,                   % the step between two line-numbers. 
                numbersep=5pt,                 % how far the line-numbers are from the code
                numberstyle=\color{black},
                    backgroundcolor=\color{black!80!white},
                rulecolor=\color{black},
                keywordstyle=\color{red}\bfseries,
                showspaces=false,               % show spaces adding particular underscores
                showstringspaces=false,         % underline spaces within strings
                showtabs=false,                 % show tabs within strings adding particular underscores
                frame=single,                   % adds a frame around the code
                framexleftmargin=0mm,
                numberblanklines=false,
                xleftmargin=5pt,
                breaklines=true,
                breakatwhitespace=true,
                breakautoindent=true,
                captionpos=t,
                texcl=true,
                tabsize=2,                      % sets default tabsize to 3 spaces
                extendedchars=true,
                inputencoding=utf8, 
                escapechar=\%,
                #1}}{\addtocounter{countOut}{1}}




            \lstnewenvironment{latex}[1][caption=Ponme caption, label=default]{
                \renewcommand*{\lstlistingname}{\LaTeX$_\epsilon$}  
                \lstset{
                language=TeX, 
                frame=t,
                basicstyle=\ttfamily\footnotesize,       % the size of the fonts that are used for the code
                numbers=left,                   % where to put the line-numbers
                breaklines=true,
                aboveskip=0pt,
                belowskip=0pt, 
                captionpos = t, #1}
            }{}




% --------------------------------------------------------------------------------------------------------------------------
% ---mdframed – Framed environments that can split at page boundaries
% --------------------------------------------------------------------------------------------------------------------------
%\RequirePackage[framemethod=TikZ]{mdframed}
\RequirePackage{mdframed}
\usetikzlibrary{calc}
\RequirePackage{chngcntr}



			


\newcounter{excounter}[chapter]\setcounter{excounter}{0}
\renewcommand{\theexcounter}{\arabic{chapter}.\arabic{excounter}}

\newenvironment{example}[2][]{%
\refstepcounter{excounter}%
\ifstrempty{#1}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=black!20, draw=black!80, line width=0.2mm]
			{\strut Ejemplo~\theexcounter};}}
	}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=black!20, draw=black!80, line width=0.2mm]
			{\strut Ejemplo~\theexcounter:~#1};}}%
	}%
	\mdfsetup{frametitleaboveskip=-0.75\baselineskip, %\dimexpr-\ht\strutbox\relax,
		skipabove=\baselineskip,
    	skipbelow=\baselineskip,
		innertopmargin=0pt,
		%innerbottommargin=0pt,
		innerleftmargin=10,
		innerrightmargin=10,
		linecolor=black!30,%
		linewidth=2pt,
		topline=true,%
		rightline=true,
		bottomline=true,
		leftline=true,
		roundcorner=1mm,
		backgroundcolor=black!3!white,
		backgroundcolor=black!3!white,
		font=\myfontEjemplo
	}
\begin{mdframed}[]\relax \label{#2}}
{\end{mdframed}}



											

\newcounter{defcounter}[chapter]\setcounter{defcounter}{0}
\renewcommand{\thedefcounter}{\arabic{chapter}.\arabic{defcounter}}

\newenvironment{definition}[2][]{%
\refstepcounter{defcounter}%
\ifstrempty{#1}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=blue!20, draw=blue!80, line width=0.2mm]
			{\strut Definición~\thedefcounter};}}
	}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=blue!20, draw=blue!80, line width=0.2mm]
			{\strut Definición~\thedefcounter:~#1};}}%
	}%
	\mdfsetup{frametitleaboveskip=-0.75\baselineskip, %\dimexpr-\ht\strutbox\relax,
		skipabove=\baselineskip,
    	skipbelow=\baselineskip,
		innertopmargin=0pt,
		%innerbottommargin=0pt,
		innerleftmargin=10,
		innerrightmargin=10,
		linecolor=blue!20,%
		linewidth=2pt,
		topline=true,%
		rightline=true,
		bottomline=true,
		leftline=true,
		roundcorner=1mm,
		backgroundcolor=blue!0,
		backgroundcolor=blue!0,
		font=\myfontEjemplo
	}
\begin{mdframed}[]\relax \label{#2}}
{\end{mdframed}}




											

\newcounter{lemmacounter}[chapter]\setcounter{lemmacounter}{0}
\renewcommand{\thelemmacounter}{\arabic{chapter}.\arabic{lemmacounter}}

\newenvironment{lemma}[2][]{%
\refstepcounter{lemmacounter}%
\ifstrempty{#1}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=blue!20, draw=blue!80, line width=0.2mm]
			{\strut Lema~\thelemmacounter};}}
	}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=blue!20, draw=blue!80, line width=0.2mm]
			{\strut Lema~\thelemmacounter:~#1};}}%
	}%
	\mdfsetup{frametitleaboveskip=-0.75\baselineskip, %\dimexpr-\ht\strutbox\relax,
		skipabove=\baselineskip,
    	skipbelow=\baselineskip,
		innertopmargin=0pt,
		%innerbottommargin=0pt,
		innerleftmargin=10,
		innerrightmargin=10,
		linecolor=blue!20,%
		linewidth=2pt,
		topline=true,%
		rightline=true,
		bottomline=true,
		leftline=true,
		roundcorner=1mm,
		backgroundcolor=blue!5,
		backgroundcolor=blue!5,
		font=\myfontEjemplo
	}
\begin{mdframed}[]\relax \label{#2}}
{\end{mdframed}}




\newcounter{thcounter}[chapter]\setcounter{thcounter}{0}
\renewcommand{\thethcounter}{\arabic{chapter}.\arabic{thcounter}}

\newenvironment{teorema}[2][]{%
\refstepcounter{thcounter}%
\ifstrempty{#1}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=red!20, draw=red!80, line width=0.2mm]
			{\strut Teorema~\thethcounter};}}
	}%
	{\mdfsetup{%
		frametitle={%
		\tikz[baseline=(current bounding box.east),outer sep=0pt]
		\node[anchor=east,rounded corners,fill=red!20, draw=red!80, line width=0.2mm]
			{\strut Teorema~\thethcounter:~#1};}}%
	}%
	\mdfsetup{frametitleaboveskip=-0.75\baselineskip, %\dimexpr-\ht\strutbox\relax,
		skipabove=\baselineskip,
    	skipbelow=\baselineskip,
		innertopmargin=0pt,
		%innerbottommargin=0pt,
		innerleftmargin=10,
		innerrightmargin=10,
		linecolor=red!50,%
		linewidth=2pt,
		topline=true,%
		rightline=true,
		bottomline=true,
		leftline=true,
		roundcorner=1mm,
		backgroundcolor=red!0,
		backgroundcolor=red!0,
		font=\myfontEjemplo
	}
\begin{mdframed}[]\relax \label{#2}}
{\end{mdframed}}






\mdfdefinestyle{mdfEjercicio}{%
	linecolor=white!50!red!90!green,%blue,
	topline=false,
	rightline=false,
	bottomline=false,
	linewidth=1.5pt,
	%innerleftmargin=15pt,
	innerrightmargin=0pt,
	innertopmargin = \topskip,
	%skipabove=1.2\baselineskip,
	frametitlerule=true,%
	%frametitlebackgroundcolor=blue!20!white,
	frametitlebackgroundcolor=white!60!red!90!green,%white!80!black!90!green,
	frametitlefont=\scshape
}

						\mdtheorem[style=mdfEjercicio]{ejercicio}{Ejercicio}[chapter]
%						\mdtheorem[style=mdfEjercicio]{exercise}{Ejercicio}[chapter]
					
					
\definecolor{DarkBlue}{rgb}{.11,.23,.60}
					
\mdfdefinestyle{mdfCode}{%
linewidth=0.0pt,
leftmargin=5pt, 
rightmargin=10pt,
innerleftmargin=20pt,
middlelinecolor=DarkBlue,
middlelinewidth=2pt,
frametitlerule=false,
backgroundcolor=black!10!white,
frametitle={Ventana de Comandos},
frametitlefont={\normalfont\sffamily\color{white}},
frametitlebackgroundcolor=DarkBlue,
%nobreak,
}
						%\mdtheorem[style=mdfCode]{code}{Processing.}
						\surroundwithmdframed[style=mdfCode]{latex}
						%\surroundwithmdframed[style=mdfCode]{JJava}


\mdfdefinestyle{mdfOutput}{%
linewidth=0.0pt,
leftmargin=5pt, 
rightmargin=10pt,
innerleftmargin=20pt,
middlelinecolor=DarkBlue,
middlelinewidth=2pt,
frametitlerule=false,
backgroundcolor=black!90!white,
fontcolor=white!90!black,
font={\normalfont\ttfamily\small},
%frametitle={\color{black} Consola},
frametitlefont={\normalfont\sffamily\color{white}},
frametitlebackgroundcolor=black!50!white,
%nobreak,
}

%\mdtheorem[style=mdfOutput]{out}{CONSOLA.}

%\newmdenv[style=mdfOutput]{out}
	
	
\mdfdefinestyle{mdfEjerPropuestos}{%
linewidth=1.5pt,
leftmargin=5pt, rightmargin=10pt,innerleftmargin=15pt,
middlelinecolor=DarkBlue,
middlelinewidth=2pt,
frametitlerule=false,
backgroundcolor=white, %orange!10!white,
frametitle={Ejercicios Propuestos.},
frametitlefont={\Large\bf\color{white}},%{\normalfont\sffamily\color{white}},
frametitlebackgroundcolor=gray, 
%nobreak,
}




							%\mdtheorem[style=mdfEjerPropuestos]{ejerciciosP}{Ejercicios Propuestos}
\newmdenv[style=mdfEjerPropuestos]{ejerciciosP}%{Ejercicios Propuestos}
\newmdenv[style=mdfEjerPropuestos, frametitle={Repaso}, linecolor=blue!70!white, frametitlebackgroundcolor=blue!70!white]{ejerciciosR}			
\newmdenv[style=mdfEjerPropuestos, frametitle={Nivel Inicial}, linecolor=green!70!black, frametitlebackgroundcolor=green!70!black]{ejerciciosPI}
\newmdenv[style=mdfEjerPropuestos, frametitle={Nivel Medio}, linecolor=orange, frametitlebackgroundcolor=orange]{ejerciciosPM}
\newmdenv[style=mdfEjerPropuestos, frametitle={Nivel Avanzado}, linecolor=red!80!black, frametitlebackgroundcolor=red!80!black]{ejerciciosPA}
\newmdenv[style=mdfEjerPropuestos, frametitle={Complementarios}, linecolor=yellow!40!blue, frametitlebackgroundcolor=yellow!40!blue]{ejerciciosC}




\mdfdefinestyle{mdfTable}{%
linewidth=1.0pt,
leftmargin=5pt, rightmargin=10pt,innerleftmargin=15pt,
middlelinecolor=DarkBlue,
middlelinewidth=2pt,
frametitlerule=false,
backgroundcolor= black!10!white,
frametitle={Salida},
frametitlefont={\normalfont\sffamily\color{white}},
frametitlebackgroundcolor=red!60!blue,
nobreak,
}




									
\newcommand{\frameleftline}{\fvset{numbers=none, frame=leftline, numbersep=2pt, framerule=0.7pt, rulecolor=\color{blue}}}
\newcommand{\framenoline}{\fvset{numbers=left, frame=none, numbersep=2pt, framerule=0.7pt}}







\mdfdefinestyle{mdfEjemplo}{%
linecolor=black,
linewidth=2.0pt,
topline=false,
rightline=false,
bottomline=false,
leftline=true,
backgroundcolor=black!3!white,
font=\myfontEjemplo,
innerleftmargin=10,
innerrightmargin=10,
frametitlerule=false,
frametitlerulecolor=white!50!green,
frametitlebackgroundcolor= black!3!white,
frametitlerulewidth=2pt}





\mdfdefinestyle{mdfImplementacion}{%
linecolor=black,
linewidth=1.0pt,
topline=true,
rightline=true,
bottomline=true,
leftline=true,
backgroundcolor=yellow!5!white,
font=\myfontEjemplo,
innerleftmargin=10,
innerrightmargin=10,
%frametitlerule=true,
%frametitlerulecolor=white!50!green,
frametitlebackgroundcolor= yellow!5!white,
frametitlerulewidth=1pt}
						\mdtheorem[style=mdfImplementacion]{implementacion}{Implementación}[chapter]
						\mdtheorem[style=mdfImplementacion]{implementation}{Implementación}[chapter]
												


\newenvironment{note}{
  \par\noindent\makebox[-3pt][r]{
    \scriptsize\color{red!90}\bcinfo\quad}
    \textbf{\color{orange}\notename} \itshape}{\par}
    
    
% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
% pythontex
% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
\usepackage[autoprint=false,autostdout=false,makestderr]{pythontex}
% \inputpygments{python}{demo.py} Para incluir ficheros.
%  how to include python scripts #27
% https://github.com/gpoore/pythontex/issues/27


% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
% Numeración en tabla de contenidos y secciones
% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
\setcounter{secnumdepth}{3}    % Number subsubsections in the chapters
\setcounter{tocdepth}{3}       % Put subsubsections in the table of contents

% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
% COMANDOS COMUNES
% -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
\newcommand{\mc}{\multicolumn}
\newcommand{\concepto}[1]{\textcolor{red!70!black}{\textbf{#1}}}
\newcommand{\key}[2][blue]{\textbf{\textcolor{#1!75!black}{#2}}}
\newcommand{\paso}[1]{\textbf{\textcolor{olive!60!magenta}{#1}}}
\newcommand{\jt}[1]{\mbox{\textcolor{blue}{#1}}\relax{}}

\definecolor{black}{rgb}{0,0,0}
\definecolor{lightgrey}{rgb}{0.925, 0.925, 0.925}
\definecolor{ForestGreen}{rgb}{0.13, 0.55, 0.13}

\newcommand{\cm}[2][ForestGreen!75!black]{\textcolor{#1}{\ttfamily \textbf{#2}}}

\newcommand{\cmbox}[2][ForestGreen!75!black]{
	\ifthenelse{\equal{#1}{verb}}
		{\colorbox{lightgrey}{\ttfamily \bfseries \!\!#2\!\!}\!}
		{\colorbox{lightgrey}{\color{#1} \ttfamily \bfseries \!\!#2\!\!}\!}
}


\newcommand{\cmboxb}[2][ForestGreen!75!black]{
	\ifthenelse{\equal{#1}{verb}}
		{\colorbox{lightgrey}{\ttfamily \bfseries \!\!#2\!\!}\!}
		{\colorbox{black}{\color{#1} \ttfamily \bfseries \!\!#2\!\!}\!}
}




\newcommand{\ds}{\displaystyle}
\newcommand{\A}{{\cal A}}
\renewcommand{\P}{{\cal P}}

\newcommand{\coloritem}[1]{\em \textcolor{red!50!yellow!90!normal text.fg}{#1}}
\newcommand{\cerrado}{\textcolor{red}{\ding{56}}}
\newcommand{\cancel}{\cerrado}
\newcommand{\abierto}{\textcolor{green}{\ding{52}}}
\newcommand{\No}{\textcolor{red!70!black}{\ding{56}}}
\newcommand{\Si}{\textcolor{green!70!black}{\ding{52}}}
\newcommand{\fallo}{\No}
\newcommand{\ok}{\Si}



% NO FUNICIONA !!!!
%\newcommand\myColorBox{lightgrey}
%\newcommand\myColorText{ForestGreen!75!black}
%\newcommand{\cmboxB}[3]{
%	\ifthenelse{\equal{#1}{}}{\renewcommand\myColorBox{lightgrey}}{\renewcommand\myColorBox{#1}}
%	\ifthenelse{\equal{#2}{}}{\renewcommand\myColorText{ForestGreen!75!black}}{\renewcommand\myColorText{#2}}
%	\!\!\!\!
%	\colorbox{\myColorBox}{\color{\myColorText} \ttfamily \bfseries #3}
%	\!\!\!\!
%}


%\newcommand*{\cmboxb}[2][ForestGreen!75!black]{\textcolor{#1}{\bfseries\ttfamily\hyphenchar\font=45\relax \sethlcolor{lightgrey} \hl{#2}}}



%\makeatletter
%\def\SOUL@hlpreamble{%
%    \setul{}{3.5ex}% increased by 1ex
%    \let\SOUL@stcolor\SOUL@hlcolor
%    \dimen@\SOUL@ulthickness
%    \dimen@i=-.75ex % increased by -0.25ex
%    \advance\dimen@i-.5\dimen@
%    \edef\SOUL@uldepth{\the\dimen@i}%
%    \let\SOUL@ulcolor\SOUL@stcolor
%    \SOUL@ulpreamble
%}
%\makeatother

\newcommand\textify[1]{%
  \global\expandafter\let\csname textify@\string#1\endcsname#1%
  \gdef#1{\ensuremath{\csname textify@\string#1\endcsname}}%
}

\typeout{######################################}
\typeout{######  EXIT LDANIELBOOK.CLS}
\typeout{######################################}






