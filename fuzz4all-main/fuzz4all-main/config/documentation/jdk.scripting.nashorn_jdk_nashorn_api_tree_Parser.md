# Interface Parser

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\Parser.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
Parser
```

Represents nashorn ECMAScript parser instance.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CompilationUnitTree
parse​(
File
file,

DiagnosticListener
listener)
throws
IOException
,

NashornException

Parses the source file and returns compilation unit tree

**Parameters:**
- file

- source file to parse
- listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.

**Returns:**
- compilation unit tree

**Throws:**
- NullPointerException

- if file is null
- IOException

- if parse source read fails
- NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### CompilationUnitTree
parse​(
Path
path,

DiagnosticListener
listener)
throws
IOException
,

NashornException

Parses the source Path and returns compilation unit tree

**Parameters:**
- path

- source Path to parse
- listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.

**Returns:**
- compilation unit tree

**Throws:**
- NullPointerException

- if path is null
- IOException

- if parse source read fails
- NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### CompilationUnitTree
parse​(
URL
url,

DiagnosticListener
listener)
throws
IOException
,

NashornException

Parses the source url and returns compilation unit tree

**Parameters:**
- url

- source file to parse
- listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.

**Returns:**
- compilation unit tree

**Throws:**
- NullPointerException

- if url is null
- IOException

- if parse source read fails
- NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### CompilationUnitTree
parse​(
String
name,

Reader
reader,

DiagnosticListener
listener)
throws
IOException
,

NashornException

Parses the reader and returns compilation unit tree

**Parameters:**
- name

- name of the source file to parse
- reader

- from which source is read
- listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.

**Returns:**
- compilation unit tree

**Throws:**
- NullPointerException

- if name or reader is null
- IOException

- if parse source read fails
- NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### CompilationUnitTree
parse​(
String
name,

String
code,

DiagnosticListener
listener)
throws
NashornException

Parses the string source and returns compilation unit tree

**Parameters:**
- name

- of the source
- code

- string source
- listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.

**Returns:**
- compilation unit tree

**Throws:**
- NullPointerException

- if name or code is null
- NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### CompilationUnitTree
parse​(
ScriptObjectMirror
scriptObj,

DiagnosticListener
listener)
throws
NashornException

Parses the source from script object and returns compilation unit tree

**Parameters:**
- scriptObj

- script object whose script and name properties are used for script source
- listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.

**Returns:**
- compilation unit tree

**Throws:**
- NullPointerException

- if scriptObj is null
- NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### static
Parser
create​(
String
... options)
throws
IllegalArgumentException

Factory method to create a new instance of Parser.

**Parameters:**
- options

- configuration options to initialize the Parser.
Currently the following options are supported:

**"--const-as-var":** treat "const" declaration as "var"
**"-dump-on-error" or "-doe":** dump stack trace on error
**"--empty-statements":** include empty statement nodes
**"--no-syntax-extensions" or "-nse":** disable ECMAScript syntax extensions
**"-scripting":** enable scripting mode extensions
**"-strict":** enable ECMAScript strict mode
**"--language=es6":** enable ECMAScript 6 parsing mode
**"--es6-module":** enable ECMAScript 6 module parsing mode. This option implies --language=es6

**Returns:**
- a new Parser instance.

**Throws:**
- NullPointerException

- if options array or any of its element is null
- IllegalArgumentException

- on unsupported option value.

---

### Additional Sections

#### Interface Parser

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
Parser
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Represents nashorn ECMAScript parser instance.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

Parser

Represents nashorn ECMAScript parser instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Parser

create

​(

String

... options)

Deprecated, for removal: This API element is subject to removal in a future version.

Factory method to create a new instance of Parser.

CompilationUnitTree

parse

​(

File

file,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source file and returns compilation unit tree

CompilationUnitTree

parse

​(

String

name,

Reader

reader,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the reader and returns compilation unit tree

CompilationUnitTree

parse

​(

String

name,

String

code,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the string source and returns compilation unit tree

CompilationUnitTree

parse

​(

URL

url,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source url and returns compilation unit tree

CompilationUnitTree

parse

​(

Path

path,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source Path and returns compilation unit tree

CompilationUnitTree

parse

​(

ScriptObjectMirror

scriptObj,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source from script object and returns compilation unit tree

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Parser

create

​(

String

... options)

Deprecated, for removal: This API element is subject to removal in a future version.

Factory method to create a new instance of Parser.

CompilationUnitTree

parse

​(

File

file,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source file and returns compilation unit tree

CompilationUnitTree

parse

​(

String

name,

Reader

reader,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the reader and returns compilation unit tree

CompilationUnitTree

parse

​(

String

name,

String

code,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the string source and returns compilation unit tree

CompilationUnitTree

parse

​(

URL

url,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source url and returns compilation unit tree

CompilationUnitTree

parse

​(

Path

path,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source Path and returns compilation unit tree

CompilationUnitTree

parse

​(

ScriptObjectMirror

scriptObj,

DiagnosticListener

listener)

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source from script object and returns compilation unit tree

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Factory method to create a new instance of Parser.

Parses the source file and returns compilation unit tree

Parses the reader and returns compilation unit tree

Parses the string source and returns compilation unit tree

Parses the source url and returns compilation unit tree

Parses the source Path and returns compilation unit tree

Parses the source from script object and returns compilation unit tree

============ METHOD DETAIL ==========

- Method Detail

- parse

```java
CompilationUnitTree
parse​(
File
file,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source file and returns compilation unit tree

**Parameters:** file

- source file to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if file is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
Path
path,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source Path and returns compilation unit tree

**Parameters:** path

- source Path to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if path is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
URL
url,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source url and returns compilation unit tree

**Parameters:** url

- source file to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if url is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
String
name,

Reader
reader,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the reader and returns compilation unit tree

**Parameters:** name

- name of the source file to parse
**Parameters:** reader

- from which source is read
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if name or reader is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
String
name,

String
code,

DiagnosticListener
listener)
throws
NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the string source and returns compilation unit tree

**Parameters:** name

- of the source
**Parameters:** code

- string source
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if name or code is null
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
ScriptObjectMirror
scriptObj,

DiagnosticListener
listener)
throws
NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source from script object and returns compilation unit tree

**Parameters:** scriptObj

- script object whose script and name properties are used for script source
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if scriptObj is null
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- create

```java
static
Parser
create​(
String
... options)
throws
IllegalArgumentException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Factory method to create a new instance of Parser.

**Parameters:** options

- configuration options to initialize the Parser.
Currently the following options are supported:

**"--const-as-var":** treat "const" declaration as "var"
**"-dump-on-error" or "-doe":** dump stack trace on error
**"--empty-statements":** include empty statement nodes
**"--no-syntax-extensions" or "-nse":** disable ECMAScript syntax extensions
**"-scripting":** enable scripting mode extensions
**"-strict":** enable ECMAScript strict mode
**"--language=es6":** enable ECMAScript 6 parsing mode
**"--es6-module":** enable ECMAScript 6 module parsing mode. This option implies --language=es6
**Returns:** a new Parser instance.
**Throws:** NullPointerException

- if options array or any of its element is null
**Throws:** IllegalArgumentException

- on unsupported option value.

Method Detail

- parse

```java
CompilationUnitTree
parse​(
File
file,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source file and returns compilation unit tree

**Parameters:** file

- source file to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if file is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
Path
path,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source Path and returns compilation unit tree

**Parameters:** path

- source Path to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if path is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
URL
url,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source url and returns compilation unit tree

**Parameters:** url

- source file to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if url is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
String
name,

Reader
reader,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the reader and returns compilation unit tree

**Parameters:** name

- name of the source file to parse
**Parameters:** reader

- from which source is read
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if name or reader is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
String
name,

String
code,

DiagnosticListener
listener)
throws
NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the string source and returns compilation unit tree

**Parameters:** name

- of the source
**Parameters:** code

- string source
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if name or code is null
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- parse

```java
CompilationUnitTree
parse​(
ScriptObjectMirror
scriptObj,

DiagnosticListener
listener)
throws
NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source from script object and returns compilation unit tree

**Parameters:** scriptObj

- script object whose script and name properties are used for script source
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if scriptObj is null
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

- create

```java
static
Parser
create​(
String
... options)
throws
IllegalArgumentException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Factory method to create a new instance of Parser.

**Parameters:** options

- configuration options to initialize the Parser.
Currently the following options are supported:

**"--const-as-var":** treat "const" declaration as "var"
**"-dump-on-error" or "-doe":** dump stack trace on error
**"--empty-statements":** include empty statement nodes
**"--no-syntax-extensions" or "-nse":** disable ECMAScript syntax extensions
**"-scripting":** enable scripting mode extensions
**"-strict":** enable ECMAScript strict mode
**"--language=es6":** enable ECMAScript 6 parsing mode
**"--es6-module":** enable ECMAScript 6 module parsing mode. This option implies --language=es6
**Returns:** a new Parser instance.
**Throws:** NullPointerException

- if options array or any of its element is null
**Throws:** IllegalArgumentException

- on unsupported option value.

---

#### Method Detail

parse

```java
CompilationUnitTree
parse​(
File
file,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source file and returns compilation unit tree

**Parameters:** file

- source file to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if file is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### parse

CompilationUnitTree

parse​(

File

file,

DiagnosticListener

listener)
throws

IOException

,

NashornException

Parses the source file and returns compilation unit tree

parse

```java
CompilationUnitTree
parse​(
Path
path,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source Path and returns compilation unit tree

**Parameters:** path

- source Path to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if path is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### parse

CompilationUnitTree

parse​(

Path

path,

DiagnosticListener

listener)
throws

IOException

,

NashornException

Parses the source Path and returns compilation unit tree

parse

```java
CompilationUnitTree
parse​(
URL
url,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source url and returns compilation unit tree

**Parameters:** url

- source file to parse
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if url is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### parse

CompilationUnitTree

parse​(

URL

url,

DiagnosticListener

listener)
throws

IOException

,

NashornException

Parses the source url and returns compilation unit tree

parse

```java
CompilationUnitTree
parse​(
String
name,

Reader
reader,

DiagnosticListener
listener)
throws
IOException
,

NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the reader and returns compilation unit tree

**Parameters:** name

- name of the source file to parse
**Parameters:** reader

- from which source is read
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if name or reader is null
**Throws:** IOException

- if parse source read fails
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### parse

CompilationUnitTree

parse​(

String

name,

Reader

reader,

DiagnosticListener

listener)
throws

IOException

,

NashornException

Parses the reader and returns compilation unit tree

parse

```java
CompilationUnitTree
parse​(
String
name,

String
code,

DiagnosticListener
listener)
throws
NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the string source and returns compilation unit tree

**Parameters:** name

- of the source
**Parameters:** code

- string source
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if name or code is null
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### parse

CompilationUnitTree

parse​(

String

name,

String

code,

DiagnosticListener

listener)
throws

NashornException

Parses the string source and returns compilation unit tree

parse

```java
CompilationUnitTree
parse​(
ScriptObjectMirror
scriptObj,

DiagnosticListener
listener)
throws
NashornException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Parses the source from script object and returns compilation unit tree

**Parameters:** scriptObj

- script object whose script and name properties are used for script source
**Parameters:** listener

- to receive diagnostic messages from the parser. This can be null.
if null is passed, a NashornException is thrown on the first parse error.
**Returns:** compilation unit tree
**Throws:** NullPointerException

- if scriptObj is null
**Throws:** NashornException

- is thrown if no listener is supplied and parser encounters error

---

#### parse

CompilationUnitTree

parse​(

ScriptObjectMirror

scriptObj,

DiagnosticListener

listener)
throws

NashornException

Parses the source from script object and returns compilation unit tree

create

```java
static
Parser
create​(
String
... options)
throws
IllegalArgumentException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Factory method to create a new instance of Parser.

**Parameters:** options

- configuration options to initialize the Parser.
Currently the following options are supported:

**"--const-as-var":** treat "const" declaration as "var"
**"-dump-on-error" or "-doe":** dump stack trace on error
**"--empty-statements":** include empty statement nodes
**"--no-syntax-extensions" or "-nse":** disable ECMAScript syntax extensions
**"-scripting":** enable scripting mode extensions
**"-strict":** enable ECMAScript strict mode
**"--language=es6":** enable ECMAScript 6 parsing mode
**"--es6-module":** enable ECMAScript 6 module parsing mode. This option implies --language=es6
**Returns:** a new Parser instance.
**Throws:** NullPointerException

- if options array or any of its element is null
**Throws:** IllegalArgumentException

- on unsupported option value.

---

#### create

static

Parser

create​(

String

... options)
throws

IllegalArgumentException

Factory method to create a new instance of Parser.

---

