# Class TextInputCallback

**Source:** `java.base\javax\security\auth\callback\TextInputCallback.html`

### Class Description

```java
public class
TextInputCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

TextInputCallback

to the

handle

method of a

CallbackHandler

to retrieve generic text
information.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public TextInputCallback​(
String
prompt)

Construct a

TextInputCallback

with a prompt.

**Parameters:**
- prompt

- the prompt used to request the information.

**Throws:**
- IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

---

#### public TextInputCallback​(
String
prompt,

String
defaultText)

Construct a

TextInputCallback

with a prompt
and default input value.

**Parameters:**
- prompt

- the prompt used to request the information.
- defaultText

- the text to be used as the default text displayed
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

defaultText

is null
or if

defaultText

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
getDefaultText()

Get the default text.

**Returns:**
- the default text, or null if this

TextInputCallback

was not instantiated with

defaultText

.

---

#### public void setText​(
String
text)

Set the retrieved text.

**Parameters:**
- text

- the retrieved text, which may be null.

**See Also:**
- getText()

---

#### public
String
getText()

Get the retrieved text.

**Returns:**
- the retrieved text, which may be null.

**See Also:**
- setText(java.lang.String)

---

### Additional Sections

#### Class TextInputCallback

java.lang.Object

- javax.security.auth.callback.TextInputCallback

javax.security.auth.callback.TextInputCallback

**All Implemented Interfaces:** Serializable

,

Callback

**Direct Known Subclasses:** RealmCallback

```java
public class
TextInputCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

TextInputCallback

to the

handle

method of a

CallbackHandler

to retrieve generic text
information.

**Since:** 1.4
**See Also:** CallbackHandler

,

Serialized Form

public class

TextInputCallback

extends

Object

implements

Callback

,

Serializable

Underlying security services instantiate and pass a

TextInputCallback

to the

handle

method of a

CallbackHandler

to retrieve generic text
information.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TextInputCallback

​(

String

prompt)

Construct a

TextInputCallback

with a prompt.

TextInputCallback

​(

String

prompt,

String

defaultText)

Construct a

TextInputCallback

with a prompt
and default input value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDefaultText

()

Get the default text.

String

getPrompt

()

Get the prompt.

String

getText

()

Get the retrieved text.

void

setText

​(

String

text)

Set the retrieved text.

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

TextInputCallback

​(

String

prompt)

Construct a

TextInputCallback

with a prompt.

TextInputCallback

​(

String

prompt,

String

defaultText)

Construct a

TextInputCallback

with a prompt
and default input value.

---

#### Constructor Summary

Construct a

TextInputCallback

with a prompt.

Construct a

TextInputCallback

with a prompt
and default input value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDefaultText

()

Get the default text.

String

getPrompt

()

Get the prompt.

String

getText

()

Get the retrieved text.

void

setText

​(

String

text)

Set the retrieved text.

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

Get the default text.

Get the prompt.

Get the retrieved text.

Set the retrieved text.

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

- TextInputCallback

```java
public TextInputCallback​(
String
prompt)
```

Construct a

TextInputCallback

with a prompt.

**Parameters:** prompt

- the prompt used to request the information.
**Throws:** IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

- TextInputCallback

```java
public TextInputCallback​(
String
prompt,

String
defaultText)
```

Construct a

TextInputCallback

with a prompt
and default input value.

**Parameters:** prompt

- the prompt used to request the information.
**Parameters:** defaultText

- the text to be used as the default text displayed
with the prompt.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

defaultText

is null
or if

defaultText

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

- getDefaultText

```java
public
String
getDefaultText()
```

Get the default text.

**Returns:** the default text, or null if this

TextInputCallback

was not instantiated with

defaultText

.

- setText

```java
public void setText​(
String
text)
```

Set the retrieved text.

**Parameters:** text

- the retrieved text, which may be null.
**See Also:** getText()

- getText

```java
public
String
getText()
```

Get the retrieved text.

**Returns:** the retrieved text, which may be null.
**See Also:** setText(java.lang.String)

Constructor Detail

- TextInputCallback

```java
public TextInputCallback​(
String
prompt)
```

Construct a

TextInputCallback

with a prompt.

**Parameters:** prompt

- the prompt used to request the information.
**Throws:** IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

- TextInputCallback

```java
public TextInputCallback​(
String
prompt,

String
defaultText)
```

Construct a

TextInputCallback

with a prompt
and default input value.

**Parameters:** prompt

- the prompt used to request the information.
**Parameters:** defaultText

- the text to be used as the default text displayed
with the prompt.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

defaultText

is null
or if

defaultText

has a length of 0.

---

#### Constructor Detail

TextInputCallback

```java
public TextInputCallback​(
String
prompt)
```

Construct a

TextInputCallback

with a prompt.

**Parameters:** prompt

- the prompt used to request the information.
**Throws:** IllegalArgumentException

- if

prompt

is null
or if

prompt

has a length of 0.

---

#### TextInputCallback

public TextInputCallback​(

String

prompt)

Construct a

TextInputCallback

with a prompt.

TextInputCallback

```java
public TextInputCallback​(
String
prompt,

String
defaultText)
```

Construct a

TextInputCallback

with a prompt
and default input value.

**Parameters:** prompt

- the prompt used to request the information.
**Parameters:** defaultText

- the text to be used as the default text displayed
with the prompt.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

defaultText

is null
or if

defaultText

has a length of 0.

---

#### TextInputCallback

public TextInputCallback​(

String

prompt,

String

defaultText)

Construct a

TextInputCallback

with a prompt
and default input value.

Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

- getDefaultText

```java
public
String
getDefaultText()
```

Get the default text.

**Returns:** the default text, or null if this

TextInputCallback

was not instantiated with

defaultText

.

- setText

```java
public void setText​(
String
text)
```

Set the retrieved text.

**Parameters:** text

- the retrieved text, which may be null.
**See Also:** getText()

- getText

```java
public
String
getText()
```

Get the retrieved text.

**Returns:** the retrieved text, which may be null.
**See Also:** setText(java.lang.String)

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

getDefaultText

```java
public
String
getDefaultText()
```

Get the default text.

**Returns:** the default text, or null if this

TextInputCallback

was not instantiated with

defaultText

.

---

#### getDefaultText

public

String

getDefaultText()

Get the default text.

setText

```java
public void setText​(
String
text)
```

Set the retrieved text.

**Parameters:** text

- the retrieved text, which may be null.
**See Also:** getText()

---

#### setText

public void setText​(

String

text)

Set the retrieved text.

getText

```java
public
String
getText()
```

Get the retrieved text.

**Returns:** the retrieved text, which may be null.
**See Also:** setText(java.lang.String)

---

#### getText

public

String

getText()

Get the retrieved text.

---

