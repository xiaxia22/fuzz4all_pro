# Class ImportSnippet

**Source:** `jdk.jshell\jdk\jshell\ImportSnippet.html`

### Class Description

```java
public class
ImportSnippet

extends
PersistentSnippet
```

Snippet for an import declaration.
The Kind is

Snippet.Kind.IMPORT

.

ImportSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9
**See The Java™ Language Specification :** 8.3: importDeclaration.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
name()

The identifying name of the import. For on-demand imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

or
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks. For single imports
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
it is the imported name. That is, the unqualified name.

**Overrides:**
- name

in class

PersistentSnippet

**Returns:**
- the name of the import.

---

#### public
String
fullname()

The qualified name of the import. For any imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

,
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

),
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks.

**Returns:**
- the fullname of the import

---

#### public boolean isStatic()

Indicates whether this snippet represents a static import.

**Returns:**
- true

if this snippet represents a static import;
otherwise

false

---

### Additional Sections

#### Class ImportSnippet

java.lang.Object

- jdk.jshell.Snippet
- - jdk.jshell.PersistentSnippet
- - jdk.jshell.ImportSnippet

jdk.jshell.Snippet

- jdk.jshell.PersistentSnippet
- - jdk.jshell.ImportSnippet

jdk.jshell.PersistentSnippet

- jdk.jshell.ImportSnippet

jdk.jshell.ImportSnippet

```java
public class
ImportSnippet

extends
PersistentSnippet
```

Snippet for an import declaration.
The Kind is

Snippet.Kind.IMPORT

.

ImportSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9
**See The Java™ Language Specification :** 8.3: importDeclaration.

public class

ImportSnippet

extends

PersistentSnippet

Snippet for an import declaration.
The Kind is

Snippet.Kind.IMPORT

.

ImportSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

ImportSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

fullname

()

The qualified name of the import.

boolean

isStatic

()

Indicates whether this snippet represents a static import.

String

name

()

The identifying name of the import.

- Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

---

#### Nested Class Summary

Nested classes/interfaces declared in class jdk.jshell.

Snippet

Snippet.Kind

,

Snippet.Status

,

Snippet.SubKind

---

#### Nested classes/interfaces declared in class jdk.jshell. Snippet

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

fullname

()

The qualified name of the import.

boolean

isStatic

()

Indicates whether this snippet represents a static import.

String

name

()

The identifying name of the import.

- Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

The qualified name of the import.

Indicates whether this snippet represents a static import.

The identifying name of the import.

Methods declared in class jdk.jshell.

Snippet

id

,

kind

,

source

,

subKind

---

#### Methods declared in class jdk.jshell. Snippet

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- name

```java
public
String
name()
```

The identifying name of the import. For on-demand imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

or
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks. For single imports
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
it is the imported name. That is, the unqualified name.

**Overrides:** name

in class

PersistentSnippet
**Returns:** the name of the import.

- fullname

```java
public
String
fullname()
```

The qualified name of the import. For any imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

,
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

),
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks.

**Returns:** the fullname of the import

- isStatic

```java
public boolean isStatic()
```

Indicates whether this snippet represents a static import.

**Returns:** true

if this snippet represents a static import;
otherwise

false

Method Detail

- name

```java
public
String
name()
```

The identifying name of the import. For on-demand imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

or
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks. For single imports
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
it is the imported name. That is, the unqualified name.

**Overrides:** name

in class

PersistentSnippet
**Returns:** the name of the import.

- fullname

```java
public
String
fullname()
```

The qualified name of the import. For any imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

,
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

),
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks.

**Returns:** the fullname of the import

- isStatic

```java
public boolean isStatic()
```

Indicates whether this snippet represents a static import.

**Returns:** true

if this snippet represents a static import;
otherwise

false

---

#### Method Detail

name

```java
public
String
name()
```

The identifying name of the import. For on-demand imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

or
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks. For single imports
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
it is the imported name. That is, the unqualified name.

**Overrides:** name

in class

PersistentSnippet
**Returns:** the name of the import.

---

#### name

public

String

name()

The identifying name of the import. For on-demand imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

or
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks. For single imports
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

),
it is the imported name. That is, the unqualified name.

fullname

```java
public
String
fullname()
```

The qualified name of the import. For any imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

,
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

),
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks.

**Returns:** the fullname of the import

---

#### fullname

public

String

fullname()

The qualified name of the import. For any imports
(

Snippet.SubKind.TYPE_IMPORT_ON_DEMAND_SUBKIND

,
(

Snippet.SubKind.STATIC_IMPORT_ON_DEMAND_SUBKIND

),
(

Snippet.SubKind.SINGLE_TYPE_IMPORT_SUBKIND

or
(

Snippet.SubKind.SINGLE_STATIC_IMPORT_SUBKIND

)
that is the full specifier including any
qualifiers and the asterisks.

isStatic

```java
public boolean isStatic()
```

Indicates whether this snippet represents a static import.

**Returns:** true

if this snippet represents a static import;
otherwise

false

---

#### isStatic

public boolean isStatic()

Indicates whether this snippet represents a static import.

---

