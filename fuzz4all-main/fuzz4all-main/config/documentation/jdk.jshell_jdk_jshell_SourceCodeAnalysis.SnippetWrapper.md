# Interface SourceCodeAnalysis.SnippetWrapper

**Source:** `jdk.jshell\jdk\jshell\SourceCodeAnalysis.SnippetWrapper.html`

### Class Description

```java
public static interface
SourceCodeAnalysis.SnippetWrapper
```

The wrapping of a snippet of Java source into valid top-level Java
source. The wrapping will always either be an import or include a
synthetic class at the top-level. If a synthetic class is generated, it
will be proceeded by the package and import declarations, and may contain
synthetic class members.

This interface, in addition to the mapped form, provides the context and
position mapping information.

**Enclosing class:** SourceCodeAnalysis

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
source()

Returns the input that is wrapped. For

wrappers(String)

,
this is the source of the snippet within the input. A variable
declaration of

N

variables will map to

N

wrappers
with the source separated.

For

wrapper(Snippet)

,
this is

Snippet.source()

.

**Returns:**
- the input source corresponding to the wrapper.

---

#### String
wrapped()

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

If the input is not a valid Snippet, this will not be a valid
class/import definition.

The source may be divided and mapped to different locations within
the wrapped source.

**Returns:**
- the source wrapped into top-level Java code

---

#### String
fullClassName()

Returns the fully qualified class name of the

wrapped()

class.
For erroneous input, a best guess is returned.

**Returns:**
- the name of the synthetic wrapped class; if an import, the
name is not defined

---

#### Snippet.Kind
kind()

Returns the

Snippet.Kind

of the

source()

.

**Returns:**
- an enum representing the general kind of snippet.

---

#### int sourceToWrappedPosition​(int pos)

Maps character position within the source to character position
within the wrapped.

**Parameters:**
- pos

- the position in

source()

**Returns:**
- the corresponding position in

wrapped()

---

#### int wrappedToSourcePosition​(int pos)

Maps character position within the wrapped to character position
within the source.

**Parameters:**
- pos

- the position in

wrapped()

**Returns:**
- the corresponding position in

source()

---

### Additional Sections

#### Interface SourceCodeAnalysis.SnippetWrapper

**Enclosing class:** SourceCodeAnalysis

```java
public static interface
SourceCodeAnalysis.SnippetWrapper
```

The wrapping of a snippet of Java source into valid top-level Java
source. The wrapping will always either be an import or include a
synthetic class at the top-level. If a synthetic class is generated, it
will be proceeded by the package and import declarations, and may contain
synthetic class members.

This interface, in addition to the mapped form, provides the context and
position mapping information.

public static interface

SourceCodeAnalysis.SnippetWrapper

The wrapping of a snippet of Java source into valid top-level Java
source. The wrapping will always either be an import or include a
synthetic class at the top-level. If a synthetic class is generated, it
will be proceeded by the package and import declarations, and may contain
synthetic class members.

This interface, in addition to the mapped form, provides the context and
position mapping information.

This interface, in addition to the mapped form, provides the context and
position mapping information.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

fullClassName

()

Returns the fully qualified class name of the

wrapped()

class.

Snippet.Kind

kind

()

Returns the

Snippet.Kind

of the

source()

.

String

source

()

Returns the input that is wrapped.

int

sourceToWrappedPosition

​(int pos)

Maps character position within the source to character position
within the wrapped.

String

wrapped

()

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

int

wrappedToSourcePosition

​(int pos)

Maps character position within the wrapped to character position
within the source.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

fullClassName

()

Returns the fully qualified class name of the

wrapped()

class.

Snippet.Kind

kind

()

Returns the

Snippet.Kind

of the

source()

.

String

source

()

Returns the input that is wrapped.

int

sourceToWrappedPosition

​(int pos)

Maps character position within the source to character position
within the wrapped.

String

wrapped

()

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

int

wrappedToSourcePosition

​(int pos)

Maps character position within the wrapped to character position
within the source.

---

#### Method Summary

Returns the fully qualified class name of the

wrapped()

class.

Returns the

Snippet.Kind

of the

source()

.

Returns the input that is wrapped.

Maps character position within the source to character position
within the wrapped.

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

Maps character position within the wrapped to character position
within the source.

============ METHOD DETAIL ==========

- Method Detail

- source

```java
String
source()
```

Returns the input that is wrapped. For

wrappers(String)

,
this is the source of the snippet within the input. A variable
declaration of

N

variables will map to

N

wrappers
with the source separated.

For

wrapper(Snippet)

,
this is

Snippet.source()

.

**Returns:** the input source corresponding to the wrapper.

- wrapped

```java
String
wrapped()
```

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

If the input is not a valid Snippet, this will not be a valid
class/import definition.

The source may be divided and mapped to different locations within
the wrapped source.

**Returns:** the source wrapped into top-level Java code

- fullClassName

```java
String
fullClassName()
```

Returns the fully qualified class name of the

wrapped()

class.
For erroneous input, a best guess is returned.

**Returns:** the name of the synthetic wrapped class; if an import, the
name is not defined

- kind

```java
Snippet.Kind
kind()
```

Returns the

Snippet.Kind

of the

source()

.

**Returns:** an enum representing the general kind of snippet.

- sourceToWrappedPosition

```java
int sourceToWrappedPosition​(int pos)
```

Maps character position within the source to character position
within the wrapped.

**Parameters:** pos

- the position in

source()
**Returns:** the corresponding position in

wrapped()

- wrappedToSourcePosition

```java
int wrappedToSourcePosition​(int pos)
```

Maps character position within the wrapped to character position
within the source.

**Parameters:** pos

- the position in

wrapped()
**Returns:** the corresponding position in

source()

Method Detail

- source

```java
String
source()
```

Returns the input that is wrapped. For

wrappers(String)

,
this is the source of the snippet within the input. A variable
declaration of

N

variables will map to

N

wrappers
with the source separated.

For

wrapper(Snippet)

,
this is

Snippet.source()

.

**Returns:** the input source corresponding to the wrapper.

- wrapped

```java
String
wrapped()
```

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

If the input is not a valid Snippet, this will not be a valid
class/import definition.

The source may be divided and mapped to different locations within
the wrapped source.

**Returns:** the source wrapped into top-level Java code

- fullClassName

```java
String
fullClassName()
```

Returns the fully qualified class name of the

wrapped()

class.
For erroneous input, a best guess is returned.

**Returns:** the name of the synthetic wrapped class; if an import, the
name is not defined

- kind

```java
Snippet.Kind
kind()
```

Returns the

Snippet.Kind

of the

source()

.

**Returns:** an enum representing the general kind of snippet.

- sourceToWrappedPosition

```java
int sourceToWrappedPosition​(int pos)
```

Maps character position within the source to character position
within the wrapped.

**Parameters:** pos

- the position in

source()
**Returns:** the corresponding position in

wrapped()

- wrappedToSourcePosition

```java
int wrappedToSourcePosition​(int pos)
```

Maps character position within the wrapped to character position
within the source.

**Parameters:** pos

- the position in

wrapped()
**Returns:** the corresponding position in

source()

---

#### Method Detail

source

```java
String
source()
```

Returns the input that is wrapped. For

wrappers(String)

,
this is the source of the snippet within the input. A variable
declaration of

N

variables will map to

N

wrappers
with the source separated.

For

wrapper(Snippet)

,
this is

Snippet.source()

.

**Returns:** the input source corresponding to the wrapper.

---

#### source

String

source()

Returns the input that is wrapped. For

wrappers(String)

,
this is the source of the snippet within the input. A variable
declaration of

N

variables will map to

N

wrappers
with the source separated.

For

wrapper(Snippet)

,
this is

Snippet.source()

.

For

wrapper(Snippet)

,
this is

Snippet.source()

.

wrapped

```java
String
wrapped()
```

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

If the input is not a valid Snippet, this will not be a valid
class/import definition.

The source may be divided and mapped to different locations within
the wrapped source.

**Returns:** the source wrapped into top-level Java code

---

#### wrapped

String

wrapped()

Returns a Java class definition that wraps the

source()

or, if an import, the import source.

If the input is not a valid Snippet, this will not be a valid
class/import definition.

The source may be divided and mapped to different locations within
the wrapped source.

If the input is not a valid Snippet, this will not be a valid
class/import definition.

The source may be divided and mapped to different locations within
the wrapped source.

The source may be divided and mapped to different locations within
the wrapped source.

fullClassName

```java
String
fullClassName()
```

Returns the fully qualified class name of the

wrapped()

class.
For erroneous input, a best guess is returned.

**Returns:** the name of the synthetic wrapped class; if an import, the
name is not defined

---

#### fullClassName

String

fullClassName()

Returns the fully qualified class name of the

wrapped()

class.
For erroneous input, a best guess is returned.

kind

```java
Snippet.Kind
kind()
```

Returns the

Snippet.Kind

of the

source()

.

**Returns:** an enum representing the general kind of snippet.

---

#### kind

Snippet.Kind

kind()

Returns the

Snippet.Kind

of the

source()

.

sourceToWrappedPosition

```java
int sourceToWrappedPosition​(int pos)
```

Maps character position within the source to character position
within the wrapped.

**Parameters:** pos

- the position in

source()
**Returns:** the corresponding position in

wrapped()

---

#### sourceToWrappedPosition

int sourceToWrappedPosition​(int pos)

Maps character position within the source to character position
within the wrapped.

wrappedToSourcePosition

```java
int wrappedToSourcePosition​(int pos)
```

Maps character position within the wrapped to character position
within the source.

**Parameters:** pos

- the position in

wrapped()
**Returns:** the corresponding position in

source()

---

#### wrappedToSourcePosition

int wrappedToSourcePosition​(int pos)

Maps character position within the wrapped to character position
within the source.

---

