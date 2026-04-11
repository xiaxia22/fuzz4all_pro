# Interface ScriptContext

**Source:** `java.scripting\javax\script\ScriptContext.html`

### Class Description

```java
public interface
ScriptContext
```

The interface whose implementing classes are used to connect Script Engines
with objects, such as scoped Bindings, in hosting applications. Each scope is a set
of named attributes whose values can be set and retrieved using the

ScriptContext

methods. ScriptContexts also expose Readers and Writers
that can be used by the ScriptEngines for input and output.

**All Known Implementing Classes:** SimpleScriptContext

---

### Field Details

#### static final int ENGINE_SCOPE

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

**See Also:**
- Constant Field Values

---

#### static final int GLOBAL_SCOPE

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void setBindings​(
Bindings
bindings,
int scope)

Associates a

Bindings

instance with a particular scope in this

ScriptContext

. Calls to the

getAttribute

and

setAttribute

methods must map to the

get

and

put

methods of the

Bindings

for the specified scope.

**Parameters:**
- bindings

- The

Bindings

to associate with the given scope
- scope

- The scope

**Throws:**
- IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in ScriptContexts of this type.
- NullPointerException

- if value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

---

#### Bindings
getBindings​(int scope)

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

**Parameters:**
- scope

- The scope

**Returns:**
- The associated

Bindings

. Returns

null

if it has not
been set.

**Throws:**
- IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in

ScriptContext

of this type.

---

#### void setAttribute​(
String
name,

Object
value,
int scope)

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Parameters:**
- name

- The name of the attribute to set
- value

- The value of the attribute
- scope

- The scope in which to set the attribute

**Throws:**
- IllegalArgumentException

- if the name is empty or if the scope is invalid.
- NullPointerException

- if the name is null.

---

#### Object
getAttribute​(
String
name,
int scope)

Gets the value of an attribute in a given scope.

**Parameters:**
- name

- The name of the attribute to retrieve.
- scope

- The scope in which to retrieve the attribute.

**Returns:**
- The value of the attribute. Returns

null

is the name
does not exist in the given scope.

**Throws:**
- IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
- NullPointerException

- if the name is null.

---

#### Object
removeAttribute​(
String
name,
int scope)

Remove an attribute in a given scope.

**Parameters:**
- name

- The name of the attribute to remove
- scope

- The scope in which to remove the attribute

**Returns:**
- The removed value.

**Throws:**
- IllegalArgumentException

- if the name is empty or if the scope is invalid.
- NullPointerException

- if the name is null.

---

#### Object
getAttribute​(
String
name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Parameters:**
- name

- The name of the attribute to retrieve.

**Returns:**
- The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.

**Throws:**
- NullPointerException

- if the name is null.
- IllegalArgumentException

- if the name is empty.

---

#### int getAttributesScope​(
String
name)

Get the lowest scope in which an attribute is defined.

**Parameters:**
- name

- Name of the attribute
.

**Returns:**
- The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.

**Throws:**
- NullPointerException

- if name is null.
- IllegalArgumentException

- if name is empty.

---

#### Writer
getWriter()

Returns the

Writer

for scripts to use when displaying output.

**Returns:**
- The

Writer

.

---

#### Writer
getErrorWriter()

Returns the

Writer

used to display error output.

**Returns:**
- The

Writer

---

#### void setWriter​(
Writer
writer)

Sets the

Writer

for scripts to use when displaying output.

**Parameters:**
- writer

- The new

Writer

.

---

#### void setErrorWriter​(
Writer
writer)

Sets the

Writer

used to display error output.

**Parameters:**
- writer

- The

Writer

.

---

#### Reader
getReader()

Returns a

Reader

to be used by the script to read
input.

**Returns:**
- The

Reader

.

---

#### void setReader​(
Reader
reader)

Sets the

Reader

for scripts to read input
.

**Parameters:**
- reader

- The new

Reader

.

---

#### List
<
Integer
> getScopes()

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

**Returns:**
- list of scope values

---

### Additional Sections

#### Interface ScriptContext

**All Known Implementing Classes:** SimpleScriptContext

```java
public interface
ScriptContext
```

The interface whose implementing classes are used to connect Script Engines
with objects, such as scoped Bindings, in hosting applications. Each scope is a set
of named attributes whose values can be set and retrieved using the

ScriptContext

methods. ScriptContexts also expose Readers and Writers
that can be used by the ScriptEngines for input and output.

**Since:** 1.6

public interface

ScriptContext

The interface whose implementing classes are used to connect Script Engines
with objects, such as scoped Bindings, in hosting applications. Each scope is a set
of named attributes whose values can be set and retrieved using the

ScriptContext

methods. ScriptContexts also expose Readers and Writers
that can be used by the ScriptEngines for input and output.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ENGINE_SCOPE

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

static int

GLOBAL_SCOPE

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getAttribute

​(

String

name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order.

Object

getAttribute

​(

String

name,
int scope)

Gets the value of an attribute in a given scope.

int

getAttributesScope

​(

String

name)

Get the lowest scope in which an attribute is defined.

Bindings

getBindings

​(int scope)

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

Writer

getErrorWriter

()

Returns the

Writer

used to display error output.

Reader

getReader

()

Returns a

Reader

to be used by the script to read
input.

List

<

Integer

>

getScopes

()

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

Writer

getWriter

()

Returns the

Writer

for scripts to use when displaying output.

Object

removeAttribute

​(

String

name,
int scope)

Remove an attribute in a given scope.

void

setAttribute

​(

String

name,

Object

value,
int scope)

Sets the value of an attribute in a given scope.

void

setBindings

​(

Bindings

bindings,
int scope)

Associates a

Bindings

instance with a particular scope in this

ScriptContext

.

void

setErrorWriter

​(

Writer

writer)

Sets the

Writer

used to display error output.

void

setReader

​(

Reader

reader)

Sets the

Reader

for scripts to read input
.

void

setWriter

​(

Writer

writer)

Sets the

Writer

for scripts to use when displaying output.

Field Summary

Fields

Modifier and Type

Field

Description

static int

ENGINE_SCOPE

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

static int

GLOBAL_SCOPE

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

---

#### Field Summary

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getAttribute

​(

String

name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order.

Object

getAttribute

​(

String

name,
int scope)

Gets the value of an attribute in a given scope.

int

getAttributesScope

​(

String

name)

Get the lowest scope in which an attribute is defined.

Bindings

getBindings

​(int scope)

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

Writer

getErrorWriter

()

Returns the

Writer

used to display error output.

Reader

getReader

()

Returns a

Reader

to be used by the script to read
input.

List

<

Integer

>

getScopes

()

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

Writer

getWriter

()

Returns the

Writer

for scripts to use when displaying output.

Object

removeAttribute

​(

String

name,
int scope)

Remove an attribute in a given scope.

void

setAttribute

​(

String

name,

Object

value,
int scope)

Sets the value of an attribute in a given scope.

void

setBindings

​(

Bindings

bindings,
int scope)

Associates a

Bindings

instance with a particular scope in this

ScriptContext

.

void

setErrorWriter

​(

Writer

writer)

Sets the

Writer

used to display error output.

void

setReader

​(

Reader

reader)

Sets the

Reader

for scripts to read input
.

void

setWriter

​(

Writer

writer)

Sets the

Writer

for scripts to use when displaying output.

---

#### Method Summary

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order.

Gets the value of an attribute in a given scope.

Get the lowest scope in which an attribute is defined.

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

Returns the

Writer

used to display error output.

Returns a

Reader

to be used by the script to read
input.

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

Returns the

Writer

for scripts to use when displaying output.

Remove an attribute in a given scope.

Sets the value of an attribute in a given scope.

Associates a

Bindings

instance with a particular scope in this

ScriptContext

.

Sets the

Writer

used to display error output.

Sets the

Reader

for scripts to read input
.

Sets the

Writer

for scripts to use when displaying output.

============ FIELD DETAIL ===========

- Field Detail

- ENGINE_SCOPE

```java
static final int ENGINE_SCOPE
```

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

**See Also:** Constant Field Values

- GLOBAL_SCOPE

```java
static final int GLOBAL_SCOPE
```

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- setBindings

```java
void setBindings​(
Bindings
bindings,
int scope)
```

Associates a

Bindings

instance with a particular scope in this

ScriptContext

. Calls to the

getAttribute

and

setAttribute

methods must map to the

get

and

put

methods of the

Bindings

for the specified scope.

**Parameters:** bindings

- The

Bindings

to associate with the given scope
**Parameters:** scope

- The scope
**Throws:** IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in ScriptContexts of this type.
**Throws:** NullPointerException

- if value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

- getBindings

```java
Bindings
getBindings​(int scope)
```

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

**Parameters:** scope

- The scope
**Returns:** The associated

Bindings

. Returns

null

if it has not
been set.
**Throws:** IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in

ScriptContext

of this type.

- setAttribute

```java
void setAttribute​(
String
name,

Object
value,
int scope)
```

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Parameters:** name

- The name of the attribute to set
**Parameters:** value

- The value of the attribute
**Parameters:** scope

- The scope in which to set the attribute
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- getAttribute

```java
Object
getAttribute​(
String
name,
int scope)
```

Gets the value of an attribute in a given scope.

**Parameters:** name

- The name of the attribute to retrieve.
**Parameters:** scope

- The scope in which to retrieve the attribute.
**Returns:** The value of the attribute. Returns

null

is the name
does not exist in the given scope.
**Throws:** IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- removeAttribute

```java
Object
removeAttribute​(
String
name,
int scope)
```

Remove an attribute in a given scope.

**Parameters:** name

- The name of the attribute to remove
**Parameters:** scope

- The scope in which to remove the attribute
**Returns:** The removed value.
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- getAttribute

```java
Object
getAttribute​(
String
name)
```

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

- getAttributesScope

```java
int getAttributesScope​(
String
name)
```

Get the lowest scope in which an attribute is defined.

**Parameters:** name

- Name of the attribute
.
**Returns:** The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if name is empty.

- getWriter

```java
Writer
getWriter()
```

Returns the

Writer

for scripts to use when displaying output.

**Returns:** The

Writer

.

- getErrorWriter

```java
Writer
getErrorWriter()
```

Returns the

Writer

used to display error output.

**Returns:** The

Writer

- setWriter

```java
void setWriter​(
Writer
writer)
```

Sets the

Writer

for scripts to use when displaying output.

**Parameters:** writer

- The new

Writer

.

- setErrorWriter

```java
void setErrorWriter​(
Writer
writer)
```

Sets the

Writer

used to display error output.

**Parameters:** writer

- The

Writer

.

- getReader

```java
Reader
getReader()
```

Returns a

Reader

to be used by the script to read
input.

**Returns:** The

Reader

.

- setReader

```java
void setReader​(
Reader
reader)
```

Sets the

Reader

for scripts to read input
.

**Parameters:** reader

- The new

Reader

.

- getScopes

```java
List
<
Integer
> getScopes()
```

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

**Returns:** list of scope values

Field Detail

- ENGINE_SCOPE

```java
static final int ENGINE_SCOPE
```

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

**See Also:** Constant Field Values

- GLOBAL_SCOPE

```java
static final int GLOBAL_SCOPE
```

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

**See Also:** Constant Field Values

---

#### Field Detail

ENGINE_SCOPE

```java
static final int ENGINE_SCOPE
```

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

**See Also:** Constant Field Values

---

#### ENGINE_SCOPE

static final int ENGINE_SCOPE

EngineScope attributes are visible during the lifetime of a single

ScriptEngine

and a set of attributes is maintained for each
engine.

GLOBAL_SCOPE

```java
static final int GLOBAL_SCOPE
```

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

**See Also:** Constant Field Values

---

#### GLOBAL_SCOPE

static final int GLOBAL_SCOPE

GlobalScope attributes are visible to all engines created by same ScriptEngineFactory.

Method Detail

- setBindings

```java
void setBindings​(
Bindings
bindings,
int scope)
```

Associates a

Bindings

instance with a particular scope in this

ScriptContext

. Calls to the

getAttribute

and

setAttribute

methods must map to the

get

and

put

methods of the

Bindings

for the specified scope.

**Parameters:** bindings

- The

Bindings

to associate with the given scope
**Parameters:** scope

- The scope
**Throws:** IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in ScriptContexts of this type.
**Throws:** NullPointerException

- if value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

- getBindings

```java
Bindings
getBindings​(int scope)
```

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

**Parameters:** scope

- The scope
**Returns:** The associated

Bindings

. Returns

null

if it has not
been set.
**Throws:** IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in

ScriptContext

of this type.

- setAttribute

```java
void setAttribute​(
String
name,

Object
value,
int scope)
```

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Parameters:** name

- The name of the attribute to set
**Parameters:** value

- The value of the attribute
**Parameters:** scope

- The scope in which to set the attribute
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- getAttribute

```java
Object
getAttribute​(
String
name,
int scope)
```

Gets the value of an attribute in a given scope.

**Parameters:** name

- The name of the attribute to retrieve.
**Parameters:** scope

- The scope in which to retrieve the attribute.
**Returns:** The value of the attribute. Returns

null

is the name
does not exist in the given scope.
**Throws:** IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- removeAttribute

```java
Object
removeAttribute​(
String
name,
int scope)
```

Remove an attribute in a given scope.

**Parameters:** name

- The name of the attribute to remove
**Parameters:** scope

- The scope in which to remove the attribute
**Returns:** The removed value.
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

- getAttribute

```java
Object
getAttribute​(
String
name)
```

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

- getAttributesScope

```java
int getAttributesScope​(
String
name)
```

Get the lowest scope in which an attribute is defined.

**Parameters:** name

- Name of the attribute
.
**Returns:** The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if name is empty.

- getWriter

```java
Writer
getWriter()
```

Returns the

Writer

for scripts to use when displaying output.

**Returns:** The

Writer

.

- getErrorWriter

```java
Writer
getErrorWriter()
```

Returns the

Writer

used to display error output.

**Returns:** The

Writer

- setWriter

```java
void setWriter​(
Writer
writer)
```

Sets the

Writer

for scripts to use when displaying output.

**Parameters:** writer

- The new

Writer

.

- setErrorWriter

```java
void setErrorWriter​(
Writer
writer)
```

Sets the

Writer

used to display error output.

**Parameters:** writer

- The

Writer

.

- getReader

```java
Reader
getReader()
```

Returns a

Reader

to be used by the script to read
input.

**Returns:** The

Reader

.

- setReader

```java
void setReader​(
Reader
reader)
```

Sets the

Reader

for scripts to read input
.

**Parameters:** reader

- The new

Reader

.

- getScopes

```java
List
<
Integer
> getScopes()
```

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

**Returns:** list of scope values

---

#### Method Detail

setBindings

```java
void setBindings​(
Bindings
bindings,
int scope)
```

Associates a

Bindings

instance with a particular scope in this

ScriptContext

. Calls to the

getAttribute

and

setAttribute

methods must map to the

get

and

put

methods of the

Bindings

for the specified scope.

**Parameters:** bindings

- The

Bindings

to associate with the given scope
**Parameters:** scope

- The scope
**Throws:** IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in ScriptContexts of this type.
**Throws:** NullPointerException

- if value of scope is

ENGINE_SCOPE

and
the specified

Bindings

is null.

---

#### setBindings

void setBindings​(

Bindings

bindings,
int scope)

Associates a

Bindings

instance with a particular scope in this

ScriptContext

. Calls to the

getAttribute

and

setAttribute

methods must map to the

get

and

put

methods of the

Bindings

for the specified scope.

getBindings

```java
Bindings
getBindings​(int scope)
```

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

**Parameters:** scope

- The scope
**Returns:** The associated

Bindings

. Returns

null

if it has not
been set.
**Throws:** IllegalArgumentException

- If no

Bindings

is defined for the
specified scope value in

ScriptContext

of this type.

---

#### getBindings

Bindings

getBindings​(int scope)

Gets the

Bindings

associated with the given scope in this

ScriptContext

.

setAttribute

```java
void setAttribute​(
String
name,

Object
value,
int scope)
```

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

**Parameters:** name

- The name of the attribute to set
**Parameters:** value

- The value of the attribute
**Parameters:** scope

- The scope in which to set the attribute
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

---

#### setAttribute

void setAttribute​(

String

name,

Object

value,
int scope)

Sets the value of an attribute in a given scope. If the scope is

GLOBAL_SCOPE

and no Bindings is set for

GLOBAL_SCOPE

, then setAttribute call is a no-op.

getAttribute

```java
Object
getAttribute​(
String
name,
int scope)
```

Gets the value of an attribute in a given scope.

**Parameters:** name

- The name of the attribute to retrieve.
**Parameters:** scope

- The scope in which to retrieve the attribute.
**Returns:** The value of the attribute. Returns

null

is the name
does not exist in the given scope.
**Throws:** IllegalArgumentException

- if the name is empty or if the value of scope is invalid.
**Throws:** NullPointerException

- if the name is null.

---

#### getAttribute

Object

getAttribute​(

String

name,
int scope)

Gets the value of an attribute in a given scope.

removeAttribute

```java
Object
removeAttribute​(
String
name,
int scope)
```

Remove an attribute in a given scope.

**Parameters:** name

- The name of the attribute to remove
**Parameters:** scope

- The scope in which to remove the attribute
**Returns:** The removed value.
**Throws:** IllegalArgumentException

- if the name is empty or if the scope is invalid.
**Throws:** NullPointerException

- if the name is null.

---

#### removeAttribute

Object

removeAttribute​(

String

name,
int scope)

Remove an attribute in a given scope.

getAttribute

```java
Object
getAttribute​(
String
name)
```

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The value of the attribute in the lowest scope for
which an attribute with the given name is defined. Returns
null if no attribute with the name exists in any scope.
**Throws:** NullPointerException

- if the name is null.
**Throws:** IllegalArgumentException

- if the name is empty.

---

#### getAttribute

Object

getAttribute​(

String

name)

Retrieves the value of the attribute with the given name in
the scope occurring earliest in the search order. The order
is determined by the numeric value of the scope parameter (lowest
scope values first.)

getAttributesScope

```java
int getAttributesScope​(
String
name)
```

Get the lowest scope in which an attribute is defined.

**Parameters:** name

- Name of the attribute
.
**Returns:** The lowest scope. Returns -1 if no attribute with the given
name is defined in any scope.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if name is empty.

---

#### getAttributesScope

int getAttributesScope​(

String

name)

Get the lowest scope in which an attribute is defined.

getWriter

```java
Writer
getWriter()
```

Returns the

Writer

for scripts to use when displaying output.

**Returns:** The

Writer

.

---

#### getWriter

Writer

getWriter()

Returns the

Writer

for scripts to use when displaying output.

getErrorWriter

```java
Writer
getErrorWriter()
```

Returns the

Writer

used to display error output.

**Returns:** The

Writer

---

#### getErrorWriter

Writer

getErrorWriter()

Returns the

Writer

used to display error output.

setWriter

```java
void setWriter​(
Writer
writer)
```

Sets the

Writer

for scripts to use when displaying output.

**Parameters:** writer

- The new

Writer

.

---

#### setWriter

void setWriter​(

Writer

writer)

Sets the

Writer

for scripts to use when displaying output.

setErrorWriter

```java
void setErrorWriter​(
Writer
writer)
```

Sets the

Writer

used to display error output.

**Parameters:** writer

- The

Writer

.

---

#### setErrorWriter

void setErrorWriter​(

Writer

writer)

Sets the

Writer

used to display error output.

getReader

```java
Reader
getReader()
```

Returns a

Reader

to be used by the script to read
input.

**Returns:** The

Reader

.

---

#### getReader

Reader

getReader()

Returns a

Reader

to be used by the script to read
input.

setReader

```java
void setReader​(
Reader
reader)
```

Sets the

Reader

for scripts to read input
.

**Parameters:** reader

- The new

Reader

.

---

#### setReader

void setReader​(

Reader

reader)

Sets the

Reader

for scripts to read input
.

getScopes

```java
List
<
Integer
> getScopes()
```

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

**Returns:** list of scope values

---

#### getScopes

List

<

Integer

> getScopes()

Returns immutable

List

of all the valid values for
scope in the ScriptContext.

---

