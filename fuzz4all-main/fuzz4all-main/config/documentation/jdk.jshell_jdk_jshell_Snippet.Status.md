# Enum Snippet.Status

**Source:** `jdk.jshell\jdk\jshell\Snippet.Status.html`

### Class Description

```java
public static enum
Snippet.Status

extends
Enum
<
Snippet.Status
>
```

Describes the current state of a Snippet.
This is a dynamic property of a Snippet within the JShell state --
thus is retrieved with a

query on {@code JShell}

.

The

Status

changes as the state changes.
For example, creation of another snippet with

eval

may resolve dependencies of this Snippet (or invalidate those dependencies), or

overwrite

this Snippet changing its

Status

.

Important properties associated with

Status

are:

isDefined()

, if it is visible to other
existing and new snippets; and

isActive()

, if, as the
JShell state changes, the snippet will update, possibly
changing

Status

.
An executable Snippet can only be executed if it is in the the

VALID

Status

.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Snippet.Status

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Snippet.Status
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Status c : Snippet.Status.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Snippet.Status
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public boolean isActive()

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked. This is more broad than

isDefined()

since a Snippet which is

RECOVERABLE_NOT_DEFINED

will be updated.

**Returns:**
- true

if the Snippet is active; otherwise

false

---

#### public boolean isDefined()

Indicates whether the snippet is currently part of the defined state
of the JShell. Is it visible to compilation of other snippets?

**Returns:**
- true

if the Snippet is defined; otherwise

false

---

### Additional Sections

#### Enum Snippet.Status

java.lang.Object

- java.lang.Enum

<

Snippet.Status

>
- - jdk.jshell.Snippet.Status

java.lang.Enum

<

Snippet.Status

>

- jdk.jshell.Snippet.Status

jdk.jshell.Snippet.Status

**All Implemented Interfaces:** Serializable

,

Comparable

<

Snippet.Status

>

**Enclosing class:** Snippet

```java
public static enum
Snippet.Status

extends
Enum
<
Snippet.Status
>
```

Describes the current state of a Snippet.
This is a dynamic property of a Snippet within the JShell state --
thus is retrieved with a

query on {@code JShell}

.

The

Status

changes as the state changes.
For example, creation of another snippet with

eval

may resolve dependencies of this Snippet (or invalidate those dependencies), or

overwrite

this Snippet changing its

Status

.

Important properties associated with

Status

are:

isDefined()

, if it is visible to other
existing and new snippets; and

isActive()

, if, as the
JShell state changes, the snippet will update, possibly
changing

Status

.
An executable Snippet can only be executed if it is in the the

VALID

Status

.

**See Also:** JShell.status(jdk.jshell.Snippet)

public static enum

Snippet.Status

extends

Enum

<

Snippet.Status

>

Describes the current state of a Snippet.
This is a dynamic property of a Snippet within the JShell state --
thus is retrieved with a

query on {@code JShell}

.

The

Status

changes as the state changes.
For example, creation of another snippet with

eval

may resolve dependencies of this Snippet (or invalidate those dependencies), or

overwrite

this Snippet changing its

Status

.

Important properties associated with

Status

are:

isDefined()

, if it is visible to other
existing and new snippets; and

isActive()

, if, as the
JShell state changes, the snippet will update, possibly
changing

Status

.
An executable Snippet can only be executed if it is in the the

VALID

Status

.

The

Status

changes as the state changes.
For example, creation of another snippet with

eval

may resolve dependencies of this Snippet (or invalidate those dependencies), or

overwrite

this Snippet changing its

Status

.

Important properties associated with

Status

are:

isDefined()

, if it is visible to other
existing and new snippets; and

isActive()

, if, as the
JShell state changes, the snippet will update, possibly
changing

Status

.
An executable Snippet can only be executed if it is in the the

VALID

Status

.

Important properties associated with

Status

are:

isDefined()

, if it is visible to other
existing and new snippets; and

isActive()

, if, as the
JShell state changes, the snippet will update, possibly
changing

Status

.
An executable Snippet can only be executed if it is in the the

VALID

Status

.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

DROPPED

The snippet is inactive because of an explicit call to
the

JShell.drop(Snippet)

.

NONEXISTENT

The snippet is inactive because it does not yet exist.

OVERWRITTEN

The snippet is inactive because it has been replaced by a new
snippet.

RECOVERABLE_DEFINED

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues in its body
(in the context of current

JShell

state).

RECOVERABLE_NOT_DEFINED

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues
(in the context of current

JShell

state).

REJECTED

The snippet is inactive because it failed compilation on initial
evaluation and it is not capable of becoming valid with further
changes to the JShell state.

VALID

The snippet is a valid snippet
(in the context of current

JShell

state).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isActive

()

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked.

boolean

isDefined

()

Indicates whether the snippet is currently part of the defined state
of the JShell.

static

Snippet.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Snippet.Status

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Enum Constant Summary

Enum Constants

Enum Constant

Description

DROPPED

The snippet is inactive because of an explicit call to
the

JShell.drop(Snippet)

.

NONEXISTENT

The snippet is inactive because it does not yet exist.

OVERWRITTEN

The snippet is inactive because it has been replaced by a new
snippet.

RECOVERABLE_DEFINED

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues in its body
(in the context of current

JShell

state).

RECOVERABLE_NOT_DEFINED

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues
(in the context of current

JShell

state).

REJECTED

The snippet is inactive because it failed compilation on initial
evaluation and it is not capable of becoming valid with further
changes to the JShell state.

VALID

The snippet is a valid snippet
(in the context of current

JShell

state).

---

#### Enum Constant Summary

The snippet is inactive because of an explicit call to
the

JShell.drop(Snippet)

.

The snippet is inactive because it does not yet exist.

The snippet is inactive because it has been replaced by a new
snippet.

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues in its body
(in the context of current

JShell

state).

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues
(in the context of current

JShell

state).

The snippet is inactive because it failed compilation on initial
evaluation and it is not capable of becoming valid with further
changes to the JShell state.

The snippet is a valid snippet
(in the context of current

JShell

state).

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isActive

()

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked.

boolean

isDefined

()

Indicates whether the snippet is currently part of the defined state
of the JShell.

static

Snippet.Status

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Snippet.Status

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked.

Indicates whether the snippet is currently part of the defined state
of the JShell.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- VALID

```java
public static final
Snippet.Status
VALID
```

The snippet is a valid snippet
(in the context of current

JShell

state).
Only snippets with

VALID

Status

can be executed (though not all

VALID

snippets have executable code).

The snippet is defined
(

isDefined() == true

).
If the snippet is a declaration or import
(

Snippet.Kind.isPersistent()

),
it is visible to other snippets

The snippet will update as dependents change
(

isActive() == true

), its
status could become

RECOVERABLE_DEFINED

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

- RECOVERABLE_DEFINED

```java
public static final
Snippet.Status
RECOVERABLE_DEFINED
```

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues in its body
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has a valid signature and it is visible to other
snippets
(

isDefined() == true

)
and thus can be referenced in existing or new snippets
but the snippet cannot be executed.
An

UnresolvedReferenceException

will be thrown on an attempt
to execute it.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

- RECOVERABLE_NOT_DEFINED

```java
public static final
Snippet.Status
RECOVERABLE_NOT_DEFINED
```

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has an invalid signature or the implementation is
otherwise unable to define it.
The snippet it is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

- DROPPED

```java
public static final
Snippet.Status
DROPPED
```

The snippet is inactive because of an explicit call to
the

JShell.drop(Snippet)

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

- OVERWRITTEN

```java
public static final
Snippet.Status
OVERWRITTEN
```

The snippet is inactive because it has been replaced by a new
snippet. This occurs when the new snippet added with

eval

matches a previous snippet.
A

TypeDeclSnippet

will match another

TypeDeclSnippet

if the names match.
For example

class X { }

will overwrite

class X { int ii; }

or

interface X { }

.
A

MethodSnippet

will match another

MethodSnippet

if the names and parameter types
match.
For example

void m(int a) { }

will overwrite

int m(int a) { return a+a; }

.
A

VarSnippet

will match another

VarSnippet

if the names match.
For example

double z;

will overwrite

long z = 2L;

.
Only a

PersistentSnippet

can have this

Status

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

- REJECTED

```java
public static final
Snippet.Status
REJECTED
```

The snippet is inactive because it failed compilation on initial
evaluation and it is not capable of becoming valid with further
changes to the JShell state.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

- NONEXISTENT

```java
public static final
Snippet.Status
NONEXISTENT
```

The snippet is inactive because it does not yet exist.
Used only in

SnippetEvent.previousStatus

for new
snippets.

JShell.status(Snippet)

will never return this

Status

.

Vacuously,

isDefined()

and

isActive()

are both defined

false

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Snippet.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Status c : Snippet.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Snippet.Status
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- isActive

```java
public boolean isActive()
```

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked. This is more broad than

isDefined()

since a Snippet which is

RECOVERABLE_NOT_DEFINED

will be updated.

**Returns:** true

if the Snippet is active; otherwise

false

- isDefined

```java
public boolean isDefined()
```

Indicates whether the snippet is currently part of the defined state
of the JShell. Is it visible to compilation of other snippets?

**Returns:** true

if the Snippet is defined; otherwise

false

Enum Constant Detail

- VALID

```java
public static final
Snippet.Status
VALID
```

The snippet is a valid snippet
(in the context of current

JShell

state).
Only snippets with

VALID

Status

can be executed (though not all

VALID

snippets have executable code).

The snippet is defined
(

isDefined() == true

).
If the snippet is a declaration or import
(

Snippet.Kind.isPersistent()

),
it is visible to other snippets

The snippet will update as dependents change
(

isActive() == true

), its
status could become

RECOVERABLE_DEFINED

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

- RECOVERABLE_DEFINED

```java
public static final
Snippet.Status
RECOVERABLE_DEFINED
```

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues in its body
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has a valid signature and it is visible to other
snippets
(

isDefined() == true

)
and thus can be referenced in existing or new snippets
but the snippet cannot be executed.
An

UnresolvedReferenceException

will be thrown on an attempt
to execute it.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

- RECOVERABLE_NOT_DEFINED

```java
public static final
Snippet.Status
RECOVERABLE_NOT_DEFINED
```

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has an invalid signature or the implementation is
otherwise unable to define it.
The snippet it is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

- DROPPED

```java
public static final
Snippet.Status
DROPPED
```

The snippet is inactive because of an explicit call to
the

JShell.drop(Snippet)

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

- OVERWRITTEN

```java
public static final
Snippet.Status
OVERWRITTEN
```

The snippet is inactive because it has been replaced by a new
snippet. This occurs when the new snippet added with

eval

matches a previous snippet.
A

TypeDeclSnippet

will match another

TypeDeclSnippet

if the names match.
For example

class X { }

will overwrite

class X { int ii; }

or

interface X { }

.
A

MethodSnippet

will match another

MethodSnippet

if the names and parameter types
match.
For example

void m(int a) { }

will overwrite

int m(int a) { return a+a; }

.
A

VarSnippet

will match another

VarSnippet

if the names match.
For example

double z;

will overwrite

long z = 2L;

.
Only a

PersistentSnippet

can have this

Status

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

- REJECTED

```java
public static final
Snippet.Status
REJECTED
```

The snippet is inactive because it failed compilation on initial
evaluation and it is not capable of becoming valid with further
changes to the JShell state.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

- NONEXISTENT

```java
public static final
Snippet.Status
NONEXISTENT
```

The snippet is inactive because it does not yet exist.
Used only in

SnippetEvent.previousStatus

for new
snippets.

JShell.status(Snippet)

will never return this

Status

.

Vacuously,

isDefined()

and

isActive()

are both defined

false

.

---

#### Enum Constant Detail

VALID

```java
public static final
Snippet.Status
VALID
```

The snippet is a valid snippet
(in the context of current

JShell

state).
Only snippets with

VALID

Status

can be executed (though not all

VALID

snippets have executable code).

The snippet is defined
(

isDefined() == true

).
If the snippet is a declaration or import
(

Snippet.Kind.isPersistent()

),
it is visible to other snippets

The snippet will update as dependents change
(

isActive() == true

), its
status could become

RECOVERABLE_DEFINED

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

---

#### VALID

public static final

Snippet.Status

VALID

The snippet is a valid snippet
(in the context of current

JShell

state).
Only snippets with

VALID

Status

can be executed (though not all

VALID

snippets have executable code).

The snippet is defined
(

isDefined() == true

).
If the snippet is a declaration or import
(

Snippet.Kind.isPersistent()

),
it is visible to other snippets

The snippet will update as dependents change
(

isActive() == true

), its
status could become

RECOVERABLE_DEFINED

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

The snippet is defined
(

isDefined() == true

).
If the snippet is a declaration or import
(

Snippet.Kind.isPersistent()

),
it is visible to other snippets

The snippet will update as dependents change
(

isActive() == true

), its
status could become

RECOVERABLE_DEFINED

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

RECOVERABLE_DEFINED

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

RECOVERABLE_DEFINED

```java
public static final
Snippet.Status
RECOVERABLE_DEFINED
```

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues in its body
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has a valid signature and it is visible to other
snippets
(

isDefined() == true

)
and thus can be referenced in existing or new snippets
but the snippet cannot be executed.
An

UnresolvedReferenceException

will be thrown on an attempt
to execute it.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

---

#### RECOVERABLE_DEFINED

public static final

Snippet.Status

RECOVERABLE_DEFINED

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues in its body
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has a valid signature and it is visible to other
snippets
(

isDefined() == true

)
and thus can be referenced in existing or new snippets
but the snippet cannot be executed.
An

UnresolvedReferenceException

will be thrown on an attempt
to execute it.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

The snippet has a valid signature and it is visible to other
snippets
(

isDefined() == true

)
and thus can be referenced in existing or new snippets
but the snippet cannot be executed.
An

UnresolvedReferenceException

will be thrown on an attempt
to execute it.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_NOT_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

RECOVERABLE_NOT_DEFINED

```java
public static final
Snippet.Status
RECOVERABLE_NOT_DEFINED
```

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has an invalid signature or the implementation is
otherwise unable to define it.
The snippet it is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

---

#### RECOVERABLE_NOT_DEFINED

public static final

Snippet.Status

RECOVERABLE_NOT_DEFINED

The snippet is a declaration snippet with potentially recoverable
unresolved references or other issues
(in the context of current

JShell

state).
Only a

DeclarationSnippet

can have this

Status

.

The snippet has an invalid signature or the implementation is
otherwise unable to define it.
The snippet it is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

The snippet has an invalid signature or the implementation is
otherwise unable to define it.
The snippet it is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

The snippet will update as dependents change
(

isActive() == true

), its
status could become

VALID

,

RECOVERABLE_DEFINED

,

DROPPED

, or

OVERWRITTEN

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

Note: both

RECOVERABLE_DEFINED

and

RECOVERABLE_NOT_DEFINED

indicate potentially recoverable errors, they differ in that, for

RECOVERABLE_DEFINED

, the snippet is

defined

.

DROPPED

```java
public static final
Snippet.Status
DROPPED
```

The snippet is inactive because of an explicit call to
the

JShell.drop(Snippet)

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

---

#### DROPPED

public static final

Snippet.Status

DROPPED

The snippet is inactive because of an explicit call to
the

JShell.drop(Snippet)

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

OVERWRITTEN

```java
public static final
Snippet.Status
OVERWRITTEN
```

The snippet is inactive because it has been replaced by a new
snippet. This occurs when the new snippet added with

eval

matches a previous snippet.
A

TypeDeclSnippet

will match another

TypeDeclSnippet

if the names match.
For example

class X { }

will overwrite

class X { int ii; }

or

interface X { }

.
A

MethodSnippet

will match another

MethodSnippet

if the names and parameter types
match.
For example

void m(int a) { }

will overwrite

int m(int a) { return a+a; }

.
A

VarSnippet

will match another

VarSnippet

if the names match.
For example

double z;

will overwrite

long z = 2L;

.
Only a

PersistentSnippet

can have this

Status

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

---

#### OVERWRITTEN

public static final

Snippet.Status

OVERWRITTEN

The snippet is inactive because it has been replaced by a new
snippet. This occurs when the new snippet added with

eval

matches a previous snippet.
A

TypeDeclSnippet

will match another

TypeDeclSnippet

if the names match.
For example

class X { }

will overwrite

class X { int ii; }

or

interface X { }

.
A

MethodSnippet

will match another

MethodSnippet

if the names and parameter types
match.
For example

void m(int a) { }

will overwrite

int m(int a) { return a+a; }

.
A

VarSnippet

will match another

VarSnippet

if the names match.
For example

double z;

will overwrite

long z = 2L;

.
Only a

PersistentSnippet

can have this

Status

.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

REJECTED

```java
public static final
Snippet.Status
REJECTED
```

The snippet is inactive because it failed compilation on initial
evaluation and it is not capable of becoming valid with further
changes to the JShell state.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

---

#### REJECTED

public static final

Snippet.Status

REJECTED

The snippet is inactive because it failed compilation on initial
evaluation and it is not capable of becoming valid with further
changes to the JShell state.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

The snippet is not visible to other snippets
(

isDefined() == false

)
and thus cannot be referenced or executed.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

The snippet will not update as dependents change
(

isActive() == false

), its

Status

will never change again.

NONEXISTENT

```java
public static final
Snippet.Status
NONEXISTENT
```

The snippet is inactive because it does not yet exist.
Used only in

SnippetEvent.previousStatus

for new
snippets.

JShell.status(Snippet)

will never return this

Status

.

Vacuously,

isDefined()

and

isActive()

are both defined

false

.

---

#### NONEXISTENT

public static final

Snippet.Status

NONEXISTENT

The snippet is inactive because it does not yet exist.
Used only in

SnippetEvent.previousStatus

for new
snippets.

JShell.status(Snippet)

will never return this

Status

.

Vacuously,

isDefined()

and

isActive()

are both defined

false

.

Vacuously,

isDefined()

and

isActive()

are both defined

false

.

Method Detail

- values

```java
public static
Snippet.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Status c : Snippet.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Snippet.Status
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- isActive

```java
public boolean isActive()
```

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked. This is more broad than

isDefined()

since a Snippet which is

RECOVERABLE_NOT_DEFINED

will be updated.

**Returns:** true

if the Snippet is active; otherwise

false

- isDefined

```java
public boolean isDefined()
```

Indicates whether the snippet is currently part of the defined state
of the JShell. Is it visible to compilation of other snippets?

**Returns:** true

if the Snippet is defined; otherwise

false

---

#### Method Detail

values

```java
public static
Snippet.Status
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Status c : Snippet.Status.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Snippet.Status

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Snippet.Status c : Snippet.Status.values())
System.out.println(c);
```

for (Snippet.Status c : Snippet.Status.values())
System.out.println(c);

valueOf

```java
public static
Snippet.Status
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

Snippet.Status

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isActive

```java
public boolean isActive()
```

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked. This is more broad than

isDefined()

since a Snippet which is

RECOVERABLE_NOT_DEFINED

will be updated.

**Returns:** true

if the Snippet is active; otherwise

false

---

#### isActive

public boolean isActive()

Indicates whether the Snippet is active, that is,
will a

persistent

snippet be re-evaluated when a new

JShell.eval(String)

or

JShell.drop(Snippet)

that could change
its status is invoked. This is more broad than

isDefined()

since a Snippet which is

RECOVERABLE_NOT_DEFINED

will be updated.

isDefined

```java
public boolean isDefined()
```

Indicates whether the snippet is currently part of the defined state
of the JShell. Is it visible to compilation of other snippets?

**Returns:** true

if the Snippet is defined; otherwise

false

---

#### isDefined

public boolean isDefined()

Indicates whether the snippet is currently part of the defined state
of the JShell. Is it visible to compilation of other snippets?

---

