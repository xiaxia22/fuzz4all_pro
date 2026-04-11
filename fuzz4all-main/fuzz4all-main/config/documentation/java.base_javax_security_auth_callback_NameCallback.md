# Class NameCallback

**Source:** `java.base\javax\security\auth\callback\NameCallback.html`

### Class Description

```java
public class
NameCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

NameCallback

to the

handle

method of a

CallbackHandler

to retrieve name information.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public NameCallback​(
String
prompt)

Construct a

NameCallback

with a prompt.

**Parameters:**
- prompt

- the prompt used to request the name.

**Throws:**
- IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

---

#### public NameCallback​(
String
prompt,

String
defaultName)

Construct a

NameCallback

with a prompt
and default name.

**Parameters:**
- prompt

- the prompt used to request the information.
- defaultName

- the name to be used as the default name displayed
with the prompt.

**Throws:**
- IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

defaultName

is null,
or if

defaultName

has a length of 0.

---

### Method Details

#### public
String
getPrompt()

Get the prompt.

**Returns:**
- the prompt.

---

#### public
String
getDefaultName()

Get the default name.

**Returns:**
- the default name, or null if this

NameCallback

was not instantiated with a

defaultName

.

---

#### public void setName​(
String
name)

Set the retrieved name.

**Parameters:**
- name

- the retrieved name (which may be null).

**See Also:**
- getName()

---

#### public
String
getName()

Get the retrieved name.

**Returns:**
- the retrieved name (which may be null)

**See Also:**
- setName(java.lang.String)

---

### Additional Sections

#### Class NameCallback

java.lang.Object

- javax.security.auth.callback.NameCallback

javax.security.auth.callback.NameCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
NameCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

NameCallback

to the

handle

method of a

CallbackHandler

to retrieve name information.

**Since:** 1.4
**See Also:** CallbackHandler

,

Serialized Form

public class

NameCallback

extends

Object

implements

Callback

,

Serializable

Underlying security services instantiate and pass a

NameCallback

to the

handle

method of a

CallbackHandler

to retrieve name information.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NameCallback

​(

String

prompt)

Construct a

NameCallback

with a prompt.

NameCallback

​(

String

prompt,

String

defaultName)

Construct a

NameCallback

with a prompt
and default name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDefaultName

()

Get the default name.

String

getName

()

Get the retrieved name.

String

getPrompt

()

Get the prompt.

void

setName

​(

String

name)

Set the retrieved name.

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

Constructor Summary

Constructors

Constructor

Description

NameCallback

​(

String

prompt)

Construct a

NameCallback

with a prompt.

NameCallback

​(

String

prompt,

String

defaultName)

Construct a

NameCallback

with a prompt
and default name.

---

#### Constructor Summary

Construct a

NameCallback

with a prompt.

Construct a

NameCallback

with a prompt
and default name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDefaultName

()

Get the default name.

String

getName

()

Get the retrieved name.

String

getPrompt

()

Get the prompt.

void

setName

​(

String

name)

Set the retrieved name.

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

Get the default name.

Get the retrieved name.

Get the prompt.

Set the retrieved name.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NameCallback

```java
public NameCallback​(
String
prompt)
```

Construct a

NameCallback

with a prompt.

**Parameters:** prompt

- the prompt used to request the name.
**Throws:** IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

- NameCallback

```java
public NameCallback​(
String
prompt,

String
defaultName)
```

Construct a

NameCallback

with a prompt
and default name.

**Parameters:** prompt

- the prompt used to request the information.
**Parameters:** defaultName

- the name to be used as the default name displayed
with the prompt.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

defaultName

is null,
or if

defaultName

has a length of 0.

============ METHOD DETAIL ==========

- Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

- getDefaultName

```java
public
String
getDefaultName()
```

Get the default name.

**Returns:** the default name, or null if this

NameCallback

was not instantiated with a

defaultName

.

- setName

```java
public void setName​(
String
name)
```

Set the retrieved name.

**Parameters:** name

- the retrieved name (which may be null).
**See Also:** getName()

- getName

```java
public
String
getName()
```

Get the retrieved name.

**Returns:** the retrieved name (which may be null)
**See Also:** setName(java.lang.String)

Constructor Detail

- NameCallback

```java
public NameCallback​(
String
prompt)
```

Construct a

NameCallback

with a prompt.

**Parameters:** prompt

- the prompt used to request the name.
**Throws:** IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

- NameCallback

```java
public NameCallback​(
String
prompt,

String
defaultName)
```

Construct a

NameCallback

with a prompt
and default name.

**Parameters:** prompt

- the prompt used to request the information.
**Parameters:** defaultName

- the name to be used as the default name displayed
with the prompt.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

defaultName

is null,
or if

defaultName

has a length of 0.

---

#### Constructor Detail

NameCallback

```java
public NameCallback​(
String
prompt)
```

Construct a

NameCallback

with a prompt.

**Parameters:** prompt

- the prompt used to request the name.
**Throws:** IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

---

#### NameCallback

public NameCallback​(

String

prompt)

Construct a

NameCallback

with a prompt.

NameCallback

```java
public NameCallback​(
String
prompt,

String
defaultName)
```

Construct a

NameCallback

with a prompt
and default name.

**Parameters:** prompt

- the prompt used to request the information.
**Parameters:** defaultName

- the name to be used as the default name displayed
with the prompt.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

defaultName

is null,
or if

defaultName

has a length of 0.

---

#### NameCallback

public NameCallback​(

String

prompt,

String

defaultName)

Construct a

NameCallback

with a prompt
and default name.

Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

- getDefaultName

```java
public
String
getDefaultName()
```

Get the default name.

**Returns:** the default name, or null if this

NameCallback

was not instantiated with a

defaultName

.

- setName

```java
public void setName​(
String
name)
```

Set the retrieved name.

**Parameters:** name

- the retrieved name (which may be null).
**See Also:** getName()

- getName

```java
public
String
getName()
```

Get the retrieved name.

**Returns:** the retrieved name (which may be null)
**See Also:** setName(java.lang.String)

---

#### Method Detail

getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

---

#### getPrompt

public

String

getPrompt()

Get the prompt.

getDefaultName

```java
public
String
getDefaultName()
```

Get the default name.

**Returns:** the default name, or null if this

NameCallback

was not instantiated with a

defaultName

.

---

#### getDefaultName

public

String

getDefaultName()

Get the default name.

setName

```java
public void setName​(
String
name)
```

Set the retrieved name.

**Parameters:** name

- the retrieved name (which may be null).
**See Also:** getName()

---

#### setName

public void setName​(

String

name)

Set the retrieved name.

getName

```java
public
String
getName()
```

Get the retrieved name.

**Returns:** the retrieved name (which may be null)
**See Also:** setName(java.lang.String)

---

#### getName

public

String

getName()

Get the retrieved name.

---

