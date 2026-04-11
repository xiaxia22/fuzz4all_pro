# Class PasswordCallback

**Source:** `java.base\javax\security\auth\callback\PasswordCallback.html`

### Class Description

```java
public class
PasswordCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

PasswordCallback

to the

handle

method of a

CallbackHandler

to retrieve password information.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public PasswordCallback​(
String
prompt,
boolean echoOn)

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

**Parameters:**
- prompt

- the prompt used to request the password.
- echoOn

- true if the password should be displayed
as it is being typed.

**Throws:**
- IllegalArgumentException

- if

prompt

is null or
if

prompt

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

#### public boolean isEchoOn()

Return whether the password
should be displayed as it is being typed.

**Returns:**
- the whether the password
should be displayed as it is being typed.

---

#### public void setPassword​(char[] password)

Set the retrieved password.

This method makes a copy of the input

password

before storing it.

**Parameters:**
- password

- the retrieved password, which may be null.

**See Also:**
- getPassword()

---

#### public char[] getPassword()

Get the retrieved password.

This method returns a copy of the retrieved password.

**Returns:**
- the retrieved password, which may be null.

**See Also:**
- setPassword(char[])

---

#### public void clearPassword()

Clear the retrieved password.

---

### Additional Sections

#### Class PasswordCallback

java.lang.Object

- javax.security.auth.callback.PasswordCallback

javax.security.auth.callback.PasswordCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
PasswordCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

PasswordCallback

to the

handle

method of a

CallbackHandler

to retrieve password information.

**Since:** 1.4
**See Also:** CallbackHandler

,

Serialized Form

public class

PasswordCallback

extends

Object

implements

Callback

,

Serializable

Underlying security services instantiate and pass a

PasswordCallback

to the

handle

method of a

CallbackHandler

to retrieve password information.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PasswordCallback

​(

String

prompt,
boolean echoOn)

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clearPassword

()

Clear the retrieved password.

char[]

getPassword

()

Get the retrieved password.

String

getPrompt

()

Get the prompt.

boolean

isEchoOn

()

Return whether the password
should be displayed as it is being typed.

void

setPassword

​(char[] password)

Set the retrieved password.

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

PasswordCallback

​(

String

prompt,
boolean echoOn)

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

---

#### Constructor Summary

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clearPassword

()

Clear the retrieved password.

char[]

getPassword

()

Get the retrieved password.

String

getPrompt

()

Get the prompt.

boolean

isEchoOn

()

Return whether the password
should be displayed as it is being typed.

void

setPassword

​(char[] password)

Set the retrieved password.

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

Clear the retrieved password.

Get the retrieved password.

Get the prompt.

Return whether the password
should be displayed as it is being typed.

Set the retrieved password.

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

- PasswordCallback

```java
public PasswordCallback​(
String
prompt,
boolean echoOn)
```

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

**Parameters:** prompt

- the prompt used to request the password.
**Parameters:** echoOn

- true if the password should be displayed
as it is being typed.
**Throws:** IllegalArgumentException

- if

prompt

is null or
if

prompt

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

- isEchoOn

```java
public boolean isEchoOn()
```

Return whether the password
should be displayed as it is being typed.

**Returns:** the whether the password
should be displayed as it is being typed.

- setPassword

```java
public void setPassword​(char[] password)
```

Set the retrieved password.

This method makes a copy of the input

password

before storing it.

**Parameters:** password

- the retrieved password, which may be null.
**See Also:** getPassword()

- getPassword

```java
public char[] getPassword()
```

Get the retrieved password.

This method returns a copy of the retrieved password.

**Returns:** the retrieved password, which may be null.
**See Also:** setPassword(char[])

- clearPassword

```java
public void clearPassword()
```

Clear the retrieved password.

Constructor Detail

- PasswordCallback

```java
public PasswordCallback​(
String
prompt,
boolean echoOn)
```

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

**Parameters:** prompt

- the prompt used to request the password.
**Parameters:** echoOn

- true if the password should be displayed
as it is being typed.
**Throws:** IllegalArgumentException

- if

prompt

is null or
if

prompt

has a length of 0.

---

#### Constructor Detail

PasswordCallback

```java
public PasswordCallback​(
String
prompt,
boolean echoOn)
```

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

**Parameters:** prompt

- the prompt used to request the password.
**Parameters:** echoOn

- true if the password should be displayed
as it is being typed.
**Throws:** IllegalArgumentException

- if

prompt

is null or
if

prompt

has a length of 0.

---

#### PasswordCallback

public PasswordCallback​(

String

prompt,
boolean echoOn)

Construct a

PasswordCallback

with a prompt
and a boolean specifying whether the password should be displayed
as it is being typed.

Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

- isEchoOn

```java
public boolean isEchoOn()
```

Return whether the password
should be displayed as it is being typed.

**Returns:** the whether the password
should be displayed as it is being typed.

- setPassword

```java
public void setPassword​(char[] password)
```

Set the retrieved password.

This method makes a copy of the input

password

before storing it.

**Parameters:** password

- the retrieved password, which may be null.
**See Also:** getPassword()

- getPassword

```java
public char[] getPassword()
```

Get the retrieved password.

This method returns a copy of the retrieved password.

**Returns:** the retrieved password, which may be null.
**See Also:** setPassword(char[])

- clearPassword

```java
public void clearPassword()
```

Clear the retrieved password.

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

isEchoOn

```java
public boolean isEchoOn()
```

Return whether the password
should be displayed as it is being typed.

**Returns:** the whether the password
should be displayed as it is being typed.

---

#### isEchoOn

public boolean isEchoOn()

Return whether the password
should be displayed as it is being typed.

setPassword

```java
public void setPassword​(char[] password)
```

Set the retrieved password.

This method makes a copy of the input

password

before storing it.

**Parameters:** password

- the retrieved password, which may be null.
**See Also:** getPassword()

---

#### setPassword

public void setPassword​(char[] password)

Set the retrieved password.

This method makes a copy of the input

password

before storing it.

This method makes a copy of the input

password

before storing it.

getPassword

```java
public char[] getPassword()
```

Get the retrieved password.

This method returns a copy of the retrieved password.

**Returns:** the retrieved password, which may be null.
**See Also:** setPassword(char[])

---

#### getPassword

public char[] getPassword()

Get the retrieved password.

This method returns a copy of the retrieved password.

This method returns a copy of the retrieved password.

clearPassword

```java
public void clearPassword()
```

Clear the retrieved password.

---

#### clearPassword

public void clearPassword()

Clear the retrieved password.

---

