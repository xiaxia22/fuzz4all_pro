# Class TextCallbackHandler

**Source:** `jdk.security.auth\com\sun\security\auth\callback\TextCallbackHandler.html`

### Class Description

```java
public class
TextCallbackHandler

extends
Object

implements
CallbackHandler
```

Prompts and reads from the command line for answers to authentication
questions.
This can be used by a JAAS application to instantiate a
CallbackHandler

**All Implemented Interfaces:** CallbackHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public TextCallbackHandler()

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.
This can be used by JAAS applications to instantiate a
CallbackHandler.

---

### Method Details

#### public void handle​(
Callback
[] callbacks)
throws
IOException
,

UnsupportedCallbackException

Handles the specified set of callbacks.

**Specified by:**
- handle

in interface

CallbackHandler

**Parameters:**
- callbacks

- the callbacks to handle

**Throws:**
- IOException

- if an input or output error occurs.
- UnsupportedCallbackException

- if the callback is not an
instance of NameCallback or PasswordCallback

---

### Additional Sections

#### Class TextCallbackHandler

java.lang.Object

- com.sun.security.auth.callback.TextCallbackHandler

com.sun.security.auth.callback.TextCallbackHandler

**All Implemented Interfaces:** CallbackHandler

```java
public class
TextCallbackHandler

extends
Object

implements
CallbackHandler
```

Prompts and reads from the command line for answers to authentication
questions.
This can be used by a JAAS application to instantiate a
CallbackHandler

**See Also:** javax.security.auth.callback

public class

TextCallbackHandler

extends

Object

implements

CallbackHandler

Prompts and reads from the command line for answers to authentication
questions.
This can be used by a JAAS application to instantiate a
CallbackHandler

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TextCallbackHandler

()

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

handle

​(

Callback

[] callbacks)

Handles the specified set of callbacks.

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

TextCallbackHandler

()

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.

---

#### Constructor Summary

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

handle

​(

Callback

[] callbacks)

Handles the specified set of callbacks.

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

Handles the specified set of callbacks.

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

- TextCallbackHandler

```java
public TextCallbackHandler()
```

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.
This can be used by JAAS applications to instantiate a
CallbackHandler.

============ METHOD DETAIL ==========

- Method Detail

- handle

```java
public void handle​(
Callback
[] callbacks)
throws
IOException
,

UnsupportedCallbackException
```

Handles the specified set of callbacks.

**Specified by:** handle

in interface

CallbackHandler
**Parameters:** callbacks

- the callbacks to handle
**Throws:** IOException

- if an input or output error occurs.
**Throws:** UnsupportedCallbackException

- if the callback is not an
instance of NameCallback or PasswordCallback

Constructor Detail

- TextCallbackHandler

```java
public TextCallbackHandler()
```

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.
This can be used by JAAS applications to instantiate a
CallbackHandler.

---

#### Constructor Detail

TextCallbackHandler

```java
public TextCallbackHandler()
```

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.
This can be used by JAAS applications to instantiate a
CallbackHandler.

---

#### TextCallbackHandler

public TextCallbackHandler()

Creates a callback handler that prompts and reads from the
command line for answers to authentication questions.
This can be used by JAAS applications to instantiate a
CallbackHandler.

Method Detail

- handle

```java
public void handle​(
Callback
[] callbacks)
throws
IOException
,

UnsupportedCallbackException
```

Handles the specified set of callbacks.

**Specified by:** handle

in interface

CallbackHandler
**Parameters:** callbacks

- the callbacks to handle
**Throws:** IOException

- if an input or output error occurs.
**Throws:** UnsupportedCallbackException

- if the callback is not an
instance of NameCallback or PasswordCallback

---

#### Method Detail

handle

```java
public void handle​(
Callback
[] callbacks)
throws
IOException
,

UnsupportedCallbackException
```

Handles the specified set of callbacks.

**Specified by:** handle

in interface

CallbackHandler
**Parameters:** callbacks

- the callbacks to handle
**Throws:** IOException

- if an input or output error occurs.
**Throws:** UnsupportedCallbackException

- if the callback is not an
instance of NameCallback or PasswordCallback

---

#### handle

public void handle​(

Callback

[] callbacks)
throws

IOException

,

UnsupportedCallbackException

Handles the specified set of callbacks.

---

