# Class DefaultFormatterFactory

**Source:** `java.desktop\javax\swing\text\DefaultFormatterFactory.html`

### Class Description

```java
public class
DefaultFormatterFactory

extends
JFormattedTextField.AbstractFormatterFactory

implements
Serializable
```

An implementation of

JFormattedTextField.AbstractFormatterFactory

.

DefaultFormatterFactory

allows specifying a number of
different

JFormattedTextField.AbstractFormatter

s that are to
be used.
The most important one is the default one
(

setDefaultFormatter

). The default formatter will be used
if a more specific formatter could not be found. The following process
is used to determine the appropriate formatter to use.

- Is the passed in value null? Use the null formatter.

Does the

JFormattedTextField

have focus? Use the edit
formatter.

Otherwise, use the display formatter.

If a non-null

AbstractFormatter

has not been found, use
the default formatter.

The following code shows how to configure a

JFormattedTextField

with two

JFormattedTextField.AbstractFormatter

s, one for display and
one for editing.

```java
JFormattedTextField.AbstractFormatter editFormatter = ...;
JFormattedTextField.AbstractFormatter displayFormatter = ...;
DefaultFormatterFactory factory = new DefaultFormatterFactory(
displayFormatter, displayFormatter, editFormatter);
JFormattedTextField tf = new JFormattedTextField(factory);
```

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultFormatterFactory()

Constructs a

DefaultFormatterFactory

.

---

#### public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

**Parameters:**
- defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.

---

#### public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

**Parameters:**
- defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
- displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.

---

#### public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:**
- defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
- displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
- editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.

---

#### public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat,

JFormattedTextField.AbstractFormatter
nullFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:**
- defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
- displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
- editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.
- nullFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has a null value.

---

### Method Details

#### public void setDefaultFormatter​(
JFormattedTextField.AbstractFormatter
atf)

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

**Parameters:**
- atf

- JFormattedTextField.AbstractFormatter used if a more
specific is not specified

---

#### public
JFormattedTextField.AbstractFormatter
getDefaultFormatter()

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

**Returns:**
- JFormattedTextField.AbstractFormatter used if a more specific
one is not specified.

---

#### public void setDisplayFormatter​(
JFormattedTextField.AbstractFormatter
atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:**
- atf

- JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

---

#### public
JFormattedTextField.AbstractFormatter
getDisplayFormatter()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:**
- JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

---

#### public void setEditFormatter​(
JFormattedTextField.AbstractFormatter
atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:**
- atf

- JFormattedTextField.AbstractFormatter to use when the
component has focus

---

#### public
JFormattedTextField.AbstractFormatter
getEditFormatter()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:**
- JFormattedTextField.AbstractFormatter to use when the
component has focus

---

#### public void setNullFormatter​(
JFormattedTextField.AbstractFormatter
atf)

Sets the formatter to use if the value of the JFormattedTextField is
null.

**Parameters:**
- atf

- JFormattedTextField.AbstractFormatter to use when
the value of the JFormattedTextField is null.

---

#### public
JFormattedTextField.AbstractFormatter
getNullFormatter()

Returns the formatter to use if the value is null.

**Returns:**
- JFormattedTextField.AbstractFormatter to use when the value is
null

---

#### public
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
source)

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

**Specified by:**
- getFormatter

in class

JFormattedTextField.AbstractFormatterFactory

**Parameters:**
- source

- JFormattedTextField requesting
JFormattedTextField.AbstractFormatter

**Returns:**
- JFormattedTextField.AbstractFormatter to handle
formatting duties.

---

### Additional Sections

#### Class DefaultFormatterFactory

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatterFactory
- - javax.swing.text.DefaultFormatterFactory

javax.swing.JFormattedTextField.AbstractFormatterFactory

- javax.swing.text.DefaultFormatterFactory

javax.swing.text.DefaultFormatterFactory

**All Implemented Interfaces:** Serializable

```java
public class
DefaultFormatterFactory

extends
JFormattedTextField.AbstractFormatterFactory

implements
Serializable
```

An implementation of

JFormattedTextField.AbstractFormatterFactory

.

DefaultFormatterFactory

allows specifying a number of
different

JFormattedTextField.AbstractFormatter

s that are to
be used.
The most important one is the default one
(

setDefaultFormatter

). The default formatter will be used
if a more specific formatter could not be found. The following process
is used to determine the appropriate formatter to use.

- Is the passed in value null? Use the null formatter.

Does the

JFormattedTextField

have focus? Use the edit
formatter.

Otherwise, use the display formatter.

If a non-null

AbstractFormatter

has not been found, use
the default formatter.

The following code shows how to configure a

JFormattedTextField

with two

JFormattedTextField.AbstractFormatter

s, one for display and
one for editing.

```java
JFormattedTextField.AbstractFormatter editFormatter = ...;
JFormattedTextField.AbstractFormatter displayFormatter = ...;
DefaultFormatterFactory factory = new DefaultFormatterFactory(
displayFormatter, displayFormatter, editFormatter);
JFormattedTextField tf = new JFormattedTextField(factory);
```

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.4
**See Also:** JFormattedTextField

,

Serialized Form

public class

DefaultFormatterFactory

extends

JFormattedTextField.AbstractFormatterFactory

implements

Serializable

An implementation of

JFormattedTextField.AbstractFormatterFactory

.

DefaultFormatterFactory

allows specifying a number of
different

JFormattedTextField.AbstractFormatter

s that are to
be used.
The most important one is the default one
(

setDefaultFormatter

). The default formatter will be used
if a more specific formatter could not be found. The following process
is used to determine the appropriate formatter to use.

- Is the passed in value null? Use the null formatter.

Does the

JFormattedTextField

have focus? Use the edit
formatter.

Otherwise, use the display formatter.

If a non-null

AbstractFormatter

has not been found, use
the default formatter.

The following code shows how to configure a

JFormattedTextField

with two

JFormattedTextField.AbstractFormatter

s, one for display and
one for editing.

```java
JFormattedTextField.AbstractFormatter editFormatter = ...;
JFormattedTextField.AbstractFormatter displayFormatter = ...;
DefaultFormatterFactory factory = new DefaultFormatterFactory(
displayFormatter, displayFormatter, editFormatter);
JFormattedTextField tf = new JFormattedTextField(factory);
```

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Is the passed in value null? Use the null formatter.

Does the

JFormattedTextField

have focus? Use the edit
formatter.

Otherwise, use the display formatter.

If a non-null

AbstractFormatter

has not been found, use
the default formatter.

The following code shows how to configure a

JFormattedTextField

with two

JFormattedTextField.AbstractFormatter

s, one for display and
one for editing.

```java
JFormattedTextField.AbstractFormatter editFormatter = ...;
JFormattedTextField.AbstractFormatter displayFormatter = ...;
DefaultFormatterFactory factory = new DefaultFormatterFactory(
displayFormatter, displayFormatter, editFormatter);
JFormattedTextField tf = new JFormattedTextField(factory);
```

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

JFormattedTextField.AbstractFormatter editFormatter = ...;
JFormattedTextField.AbstractFormatter displayFormatter = ...;
DefaultFormatterFactory factory = new DefaultFormatterFactory(
displayFormatter, displayFormatter, editFormatter);
JFormattedTextField tf = new JFormattedTextField(factory);

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultFormatterFactory

()

Constructs a

DefaultFormatterFactory

.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat,

JFormattedTextField.AbstractFormatter

editFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat,

JFormattedTextField.AbstractFormatter

editFormat,

JFormattedTextField.AbstractFormatter

nullFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JFormattedTextField.AbstractFormatter

getDefaultFormatter

()

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

JFormattedTextField.AbstractFormatter

getDisplayFormatter

()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

JFormattedTextField.AbstractFormatter

getEditFormatter

()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

JFormattedTextField.AbstractFormatter

getFormatter

​(

JFormattedTextField

source)

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

JFormattedTextField.AbstractFormatter

getNullFormatter

()

Returns the formatter to use if the value is null.

void

setDefaultFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

void

setDisplayFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

void

setEditFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

void

setNullFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the formatter to use if the value of the JFormattedTextField is
null.

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

DefaultFormatterFactory

()

Constructs a

DefaultFormatterFactory

.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat,

JFormattedTextField.AbstractFormatter

editFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

DefaultFormatterFactory

​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat,

JFormattedTextField.AbstractFormatter

editFormat,

JFormattedTextField.AbstractFormatter

nullFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

---

#### Constructor Summary

Constructs a

DefaultFormatterFactory

.

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JFormattedTextField.AbstractFormatter

getDefaultFormatter

()

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

JFormattedTextField.AbstractFormatter

getDisplayFormatter

()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

JFormattedTextField.AbstractFormatter

getEditFormatter

()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

JFormattedTextField.AbstractFormatter

getFormatter

​(

JFormattedTextField

source)

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

JFormattedTextField.AbstractFormatter

getNullFormatter

()

Returns the formatter to use if the value is null.

void

setDefaultFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

void

setDisplayFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

void

setEditFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

void

setNullFormatter

​(

JFormattedTextField.AbstractFormatter

atf)

Sets the formatter to use if the value of the JFormattedTextField is
null.

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

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

Returns the formatter to use if the value is null.

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

Sets the formatter to use if the value of the JFormattedTextField is
null.

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

- DefaultFormatterFactory

```java
public DefaultFormatterFactory()
```

Constructs a

DefaultFormatterFactory

.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat)
```

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat)
```

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat)
```

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
**Parameters:** editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat,

JFormattedTextField.AbstractFormatter
nullFormat)
```

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
**Parameters:** editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.
**Parameters:** nullFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has a null value.

============ METHOD DETAIL ==========

- Method Detail

- setDefaultFormatter

```java
public void setDefaultFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter used if a more
specific is not specified

- getDefaultFormatter

```java
public
JFormattedTextField.AbstractFormatter
getDefaultFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter used if a more specific
one is not specified.

- setDisplayFormatter

```java
public void setDisplayFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

- getDisplayFormatter

```java
public
JFormattedTextField.AbstractFormatter
getDisplayFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

- setEditFormatter

```java
public void setEditFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when the
component has focus

- getEditFormatter

```java
public
JFormattedTextField.AbstractFormatter
getEditFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter to use when the
component has focus

- setNullFormatter

```java
public void setNullFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the formatter to use if the value of the JFormattedTextField is
null.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when
the value of the JFormattedTextField is null.

- getNullFormatter

```java
public
JFormattedTextField.AbstractFormatter
getNullFormatter()
```

Returns the formatter to use if the value is null.

**Returns:** JFormattedTextField.AbstractFormatter to use when the value is
null

- getFormatter

```java
public
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
source)
```

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

**Specified by:** getFormatter

in class

JFormattedTextField.AbstractFormatterFactory
**Parameters:** source

- JFormattedTextField requesting
JFormattedTextField.AbstractFormatter
**Returns:** JFormattedTextField.AbstractFormatter to handle
formatting duties.

Constructor Detail

- DefaultFormatterFactory

```java
public DefaultFormatterFactory()
```

Constructs a

DefaultFormatterFactory

.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat)
```

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat)
```

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat)
```

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
**Parameters:** editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.

- DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat,

JFormattedTextField.AbstractFormatter
nullFormat)
```

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
**Parameters:** editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.
**Parameters:** nullFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has a null value.

---

#### Constructor Detail

DefaultFormatterFactory

```java
public DefaultFormatterFactory()
```

Constructs a

DefaultFormatterFactory

.

---

#### DefaultFormatterFactory

public DefaultFormatterFactory()

Constructs a

DefaultFormatterFactory

.

DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat)
```

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.

---

#### DefaultFormatterFactory

public DefaultFormatterFactory​(

JFormattedTextField.AbstractFormatter

defaultFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

.

DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat)
```

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.

---

#### DefaultFormatterFactory

public DefaultFormatterFactory​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat)

Creates a

DefaultFormatterFactory

with the specified

JFormattedTextField.AbstractFormatter

s.

DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat)
```

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
**Parameters:** editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.

---

#### DefaultFormatterFactory

public DefaultFormatterFactory​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat,

JFormattedTextField.AbstractFormatter

editFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

DefaultFormatterFactory

```java
public DefaultFormatterFactory​(
JFormattedTextField.AbstractFormatter
defaultFormat,

JFormattedTextField.AbstractFormatter
displayFormat,

JFormattedTextField.AbstractFormatter
editFormat,

JFormattedTextField.AbstractFormatter
nullFormat)
```

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

**Parameters:** defaultFormat

- JFormattedTextField.AbstractFormatter to be used
if a more specific
JFormattedTextField.AbstractFormatter can not be
found.
**Parameters:** displayFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField does not have focus.
**Parameters:** editFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has focus.
**Parameters:** nullFormat

- JFormattedTextField.AbstractFormatter to be used
when the JFormattedTextField has a null value.

---

#### DefaultFormatterFactory

public DefaultFormatterFactory​(

JFormattedTextField.AbstractFormatter

defaultFormat,

JFormattedTextField.AbstractFormatter

displayFormat,

JFormattedTextField.AbstractFormatter

editFormat,

JFormattedTextField.AbstractFormatter

nullFormat)

Creates a DefaultFormatterFactory with the specified
JFormattedTextField.AbstractFormatters.

Method Detail

- setDefaultFormatter

```java
public void setDefaultFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter used if a more
specific is not specified

- getDefaultFormatter

```java
public
JFormattedTextField.AbstractFormatter
getDefaultFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter used if a more specific
one is not specified.

- setDisplayFormatter

```java
public void setDisplayFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

- getDisplayFormatter

```java
public
JFormattedTextField.AbstractFormatter
getDisplayFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

- setEditFormatter

```java
public void setEditFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when the
component has focus

- getEditFormatter

```java
public
JFormattedTextField.AbstractFormatter
getEditFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter to use when the
component has focus

- setNullFormatter

```java
public void setNullFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the formatter to use if the value of the JFormattedTextField is
null.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when
the value of the JFormattedTextField is null.

- getNullFormatter

```java
public
JFormattedTextField.AbstractFormatter
getNullFormatter()
```

Returns the formatter to use if the value is null.

**Returns:** JFormattedTextField.AbstractFormatter to use when the value is
null

- getFormatter

```java
public
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
source)
```

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

**Specified by:** getFormatter

in class

JFormattedTextField.AbstractFormatterFactory
**Parameters:** source

- JFormattedTextField requesting
JFormattedTextField.AbstractFormatter
**Returns:** JFormattedTextField.AbstractFormatter to handle
formatting duties.

---

#### Method Detail

setDefaultFormatter

```java
public void setDefaultFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter used if a more
specific is not specified

---

#### setDefaultFormatter

public void setDefaultFormatter​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use as
a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been
specified.

getDefaultFormatter

```java
public
JFormattedTextField.AbstractFormatter
getDefaultFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter used if a more specific
one is not specified.

---

#### getDefaultFormatter

public

JFormattedTextField.AbstractFormatter

getDefaultFormatter()

Returns the

JFormattedTextField.AbstractFormatter

to use
as a last resort, eg in case a display, edit or null

JFormattedTextField.AbstractFormatter

has not been specified.

setDisplayFormatter

```java
public void setDisplayFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

---

#### setDisplayFormatter

public void setDisplayFormatter​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

getDisplayFormatter

```java
public
JFormattedTextField.AbstractFormatter
getDisplayFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter to use when the
JFormattedTextField does not have focus

---

#### getDisplayFormatter

public

JFormattedTextField.AbstractFormatter

getDisplayFormatter()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is not being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

setEditFormatter

```java
public void setEditFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when the
component has focus

---

#### setEditFormatter

public void setEditFormatter​(

JFormattedTextField.AbstractFormatter

atf)

Sets the

JFormattedTextField.AbstractFormatter

to use if
the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

getEditFormatter

```java
public
JFormattedTextField.AbstractFormatter
getEditFormatter()
```

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

**Returns:** JFormattedTextField.AbstractFormatter to use when the
component has focus

---

#### getEditFormatter

public

JFormattedTextField.AbstractFormatter

getEditFormatter()

Returns the

JFormattedTextField.AbstractFormatter

to use
if the

JFormattedTextField

is being edited and either
the value is not-null, or the value is null and a null formatter has
has not been specified.

setNullFormatter

```java
public void setNullFormatter​(
JFormattedTextField.AbstractFormatter
atf)
```

Sets the formatter to use if the value of the JFormattedTextField is
null.

**Parameters:** atf

- JFormattedTextField.AbstractFormatter to use when
the value of the JFormattedTextField is null.

---

#### setNullFormatter

public void setNullFormatter​(

JFormattedTextField.AbstractFormatter

atf)

Sets the formatter to use if the value of the JFormattedTextField is
null.

getNullFormatter

```java
public
JFormattedTextField.AbstractFormatter
getNullFormatter()
```

Returns the formatter to use if the value is null.

**Returns:** JFormattedTextField.AbstractFormatter to use when the value is
null

---

#### getNullFormatter

public

JFormattedTextField.AbstractFormatter

getNullFormatter()

Returns the formatter to use if the value is null.

getFormatter

```java
public
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
source)
```

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

**Specified by:** getFormatter

in class

JFormattedTextField.AbstractFormatterFactory
**Parameters:** source

- JFormattedTextField requesting
JFormattedTextField.AbstractFormatter
**Returns:** JFormattedTextField.AbstractFormatter to handle
formatting duties.

---

#### getFormatter

public

JFormattedTextField.AbstractFormatter

getFormatter​(

JFormattedTextField

source)

Returns either the default formatter, display formatter, editor
formatter or null formatter based on the state of the
JFormattedTextField.

---

