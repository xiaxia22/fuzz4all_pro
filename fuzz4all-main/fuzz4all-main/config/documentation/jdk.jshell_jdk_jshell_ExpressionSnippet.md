# Class ExpressionSnippet

**Source:** `jdk.jshell\jdk\jshell\ExpressionSnippet.html`

### Class Description

```java
public class
ExpressionSnippet

extends
Snippet
```

Snippet for an assignment or variable-value expression.
The Kind is

Snippet.Kind.EXPRESSION

.

ExpressionSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9
**See The Java™ Language Specification :** 15: Expression.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
name()

Variable name which is the value of the expression. Since the expression
is either just a variable identifier or it is an assignment
to a variable, there is always a variable which is the subject of the
expression. All other forms of expression become temporary variables
which are instead referenced by a

VarSnippet

.

**Returns:**
- the name of the variable which is the subject of the expression.

---

#### public
String
typeName()

Type of the expression

**Returns:**
- String representation of the type of the expression.

---

### Additional Sections

#### Class ExpressionSnippet

java.lang.Object

- jdk.jshell.Snippet
- - jdk.jshell.ExpressionSnippet

jdk.jshell.Snippet

- jdk.jshell.ExpressionSnippet

jdk.jshell.ExpressionSnippet

```java
public class
ExpressionSnippet

extends
Snippet
```

Snippet for an assignment or variable-value expression.
The Kind is

Snippet.Kind.EXPRESSION

.

ExpressionSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

**Since:** 9
**See The Java™ Language Specification :** 15: Expression.

public class

ExpressionSnippet

extends

Snippet

Snippet for an assignment or variable-value expression.
The Kind is

Snippet.Kind.EXPRESSION

.

ExpressionSnippet

is immutable: an access to
any of its methods will always return the same result.
and thus is thread-safe.

ExpressionSnippet

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

name

()

Variable name which is the value of the expression.

String

typeName

()

Type of the expression

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

name

()

Variable name which is the value of the expression.

String

typeName

()

Type of the expression

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

Variable name which is the value of the expression.

Type of the expression

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

Variable name which is the value of the expression. Since the expression
is either just a variable identifier or it is an assignment
to a variable, there is always a variable which is the subject of the
expression. All other forms of expression become temporary variables
which are instead referenced by a

VarSnippet

.

**Returns:** the name of the variable which is the subject of the expression.

- typeName

```java
public
String
typeName()
```

Type of the expression

**Returns:** String representation of the type of the expression.

Method Detail

- name

```java
public
String
name()
```

Variable name which is the value of the expression. Since the expression
is either just a variable identifier or it is an assignment
to a variable, there is always a variable which is the subject of the
expression. All other forms of expression become temporary variables
which are instead referenced by a

VarSnippet

.

**Returns:** the name of the variable which is the subject of the expression.

- typeName

```java
public
String
typeName()
```

Type of the expression

**Returns:** String representation of the type of the expression.

---

#### Method Detail

name

```java
public
String
name()
```

Variable name which is the value of the expression. Since the expression
is either just a variable identifier or it is an assignment
to a variable, there is always a variable which is the subject of the
expression. All other forms of expression become temporary variables
which are instead referenced by a

VarSnippet

.

**Returns:** the name of the variable which is the subject of the expression.

---

#### name

public

String

name()

Variable name which is the value of the expression. Since the expression
is either just a variable identifier or it is an assignment
to a variable, there is always a variable which is the subject of the
expression. All other forms of expression become temporary variables
which are instead referenced by a

VarSnippet

.

typeName

```java
public
String
typeName()
```

Type of the expression

**Returns:** String representation of the type of the expression.

---

#### typeName

public

String

typeName()

Type of the expression

---

