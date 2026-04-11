# Class DefaultFormatter

**Source:** `java.desktop\javax\swing\text\DefaultFormatter.html`

### Class Description

```java
public class
DefaultFormatter

extends
JFormattedTextField.AbstractFormatter

implements
Cloneable
,
Serializable
```

DefaultFormatter

formats arbitrary objects. Formatting is done
by invoking the

toString

method. In order to convert the
value back to a String, your class must provide a constructor that
takes a String argument. If no single argument constructor that takes a
String is found, the returned value will be the String passed into

stringToValue

.

Instances of

DefaultFormatter

can not be used in multiple
instances of

JFormattedTextField

. To obtain a copy of
an already configured

DefaultFormatter

, use the

clone

method.

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

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultFormatter()

Creates a DefaultFormatter.

---

### Method Details

#### public void install​(
JFormattedTextField
ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:**
- install

in class

JFormattedTextField.AbstractFormatter

**Parameters:**
- ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

---

#### public void setCommitsOnValidEdit​(boolean commit)

Sets when edits are published back to the

JFormattedTextField

. If true,

commitEdit

is invoked after every valid edit (any time the text is edited). On
the other hand, if this is false than the

DefaultFormatter

does not publish edits back to the

JFormattedTextField

.
As such, the only time the value of the

JFormattedTextField

will change is when

commitEdit

is invoked on

JFormattedTextField

, typically when enter is pressed
or focus leaves the

JFormattedTextField

.

**Parameters:**
- commit

- Used to indicate when edits are committed back to the
JTextComponent

---

#### public boolean getCommitsOnValidEdit()

Returns when edits are published back to the

JFormattedTextField

.

**Returns:**
- true if edits are committed after every valid edit

---

#### public void setOverwriteMode​(boolean overwriteMode)

Configures the behavior when inserting characters. If

overwriteMode

is true (the default), new characters
overwrite existing characters in the model.

**Parameters:**
- overwriteMode

- Indicates if overwrite or overstrike mode is used

---

#### public boolean getOverwriteMode()

Returns the behavior when inserting characters.

**Returns:**
- true if newly inserted characters overwrite existing characters

---

#### public void setAllowsInvalid​(boolean allowsInvalid)

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).
It is often convenient to allow the user to temporarily input an
invalid value.

**Parameters:**
- allowsInvalid

- Used to indicate if the edited value must always
be valid

---

#### public boolean getAllowsInvalid()

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

**Returns:**
- false if the edited value must always be valid

---

#### public void setValueClass​(
Class
<?> valueClass)

Sets that class that is used to create new Objects. If the
passed in class does not have a single argument constructor that
takes a String, String values will be used.

**Parameters:**
- valueClass

- Class used to construct return value from
stringToValue

---

#### public
Class
<?> getValueClass()

Returns that class that is used to create new Objects.

**Returns:**
- Class used to construct return value from stringToValue

---

#### public
Object
stringToValue​(
String
string)
throws
ParseException

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument. If

getValueClass

returns null, the Class of the current value in the

JFormattedTextField

will be used. If this is null, a
String will be returned. If the constructor throws an exception, a

ParseException

will be thrown. If there is no single
argument String constructor,

string

will be returned.

**Specified by:**
- stringToValue

in class

JFormattedTextField.AbstractFormatter

**Parameters:**
- string

- String to convert

**Returns:**
- Object representation of text

**Throws:**
- ParseException

- if there is an error in the conversion

---

#### public
String
valueToString​(
Object
value)
throws
ParseException

Converts the passed in Object into a String by way of the

toString

method.

**Specified by:**
- valueToString

in class

JFormattedTextField.AbstractFormatter

**Parameters:**
- value

- Value to convert

**Returns:**
- String representation of value

**Throws:**
- ParseException

- if there is an error in the conversion

---

#### protected
DocumentFilter
getDocumentFilter()

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

**Overrides:**
- getDocumentFilter

in class

JFormattedTextField.AbstractFormatter

**Returns:**
- DocumentFilter to restrict edits

---

#### protected
NavigationFilter
getNavigationFilter()

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

**Overrides:**
- getNavigationFilter

in class

JFormattedTextField.AbstractFormatter

**Returns:**
- NavigationFilter to restrict navigation

---

#### public
Object
clone()
throws
CloneNotSupportedException

Creates a copy of the DefaultFormatter.

**Overrides:**
- clone

in class

JFormattedTextField.AbstractFormatter

**Returns:**
- copy of the DefaultFormatter

**Throws:**
- CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class DefaultFormatter

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatter
- - javax.swing.text.DefaultFormatter

javax.swing.JFormattedTextField.AbstractFormatter

- javax.swing.text.DefaultFormatter

javax.swing.text.DefaultFormatter

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** InternationalFormatter

,

MaskFormatter

```java
public class
DefaultFormatter

extends
JFormattedTextField.AbstractFormatter

implements
Cloneable
,
Serializable
```

DefaultFormatter

formats arbitrary objects. Formatting is done
by invoking the

toString

method. In order to convert the
value back to a String, your class must provide a constructor that
takes a String argument. If no single argument constructor that takes a
String is found, the returned value will be the String passed into

stringToValue

.

Instances of

DefaultFormatter

can not be used in multiple
instances of

JFormattedTextField

. To obtain a copy of
an already configured

DefaultFormatter

, use the

clone

method.

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
**See Also:** JFormattedTextField.AbstractFormatter

,

Serialized Form

public class

DefaultFormatter

extends

JFormattedTextField.AbstractFormatter

implements

Cloneable

,

Serializable

DefaultFormatter

formats arbitrary objects. Formatting is done
by invoking the

toString

method. In order to convert the
value back to a String, your class must provide a constructor that
takes a String argument. If no single argument constructor that takes a
String is found, the returned value will be the String passed into

stringToValue

.

Instances of

DefaultFormatter

can not be used in multiple
instances of

JFormattedTextField

. To obtain a copy of
an already configured

DefaultFormatter

, use the

clone

method.

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

Instances of

DefaultFormatter

can not be used in multiple
instances of

JFormattedTextField

. To obtain a copy of
an already configured

DefaultFormatter

, use the

clone

method.

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

DefaultFormatter

()

Creates a DefaultFormatter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the DefaultFormatter.

boolean

getAllowsInvalid

()

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

boolean

getCommitsOnValidEdit

()

Returns when edits are published back to the

JFormattedTextField

.

protected

DocumentFilter

getDocumentFilter

()

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

protected

NavigationFilter

getNavigationFilter

()

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

boolean

getOverwriteMode

()

Returns the behavior when inserting characters.

Class

<?>

getValueClass

()

Returns that class that is used to create new Objects.

void

install

​(

JFormattedTextField

ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.

void

setAllowsInvalid

​(boolean allowsInvalid)

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).

void

setCommitsOnValidEdit

​(boolean commit)

Sets when edits are published back to the

JFormattedTextField

.

void

setOverwriteMode

​(boolean overwriteMode)

Configures the behavior when inserting characters.

void

setValueClass

​(

Class

<?> valueClass)

Sets that class that is used to create new Objects.

Object

stringToValue

​(

String

string)

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument.

String

valueToString

​(

Object

value)

Converts the passed in Object into a String by way of the

toString

method.

- Methods declared in class javax.swing.

JFormattedTextField.AbstractFormatter

getActions

,

getFormattedTextField

,

invalidEdit

,

setEditValid

,

uninstall

- Methods declared in class java.lang.

Object

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

DefaultFormatter

()

Creates a DefaultFormatter.

---

#### Constructor Summary

Creates a DefaultFormatter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a copy of the DefaultFormatter.

boolean

getAllowsInvalid

()

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

boolean

getCommitsOnValidEdit

()

Returns when edits are published back to the

JFormattedTextField

.

protected

DocumentFilter

getDocumentFilter

()

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

protected

NavigationFilter

getNavigationFilter

()

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

boolean

getOverwriteMode

()

Returns the behavior when inserting characters.

Class

<?>

getValueClass

()

Returns that class that is used to create new Objects.

void

install

​(

JFormattedTextField

ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.

void

setAllowsInvalid

​(boolean allowsInvalid)

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).

void

setCommitsOnValidEdit

​(boolean commit)

Sets when edits are published back to the

JFormattedTextField

.

void

setOverwriteMode

​(boolean overwriteMode)

Configures the behavior when inserting characters.

void

setValueClass

​(

Class

<?> valueClass)

Sets that class that is used to create new Objects.

Object

stringToValue

​(

String

string)

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument.

String

valueToString

​(

Object

value)

Converts the passed in Object into a String by way of the

toString

method.

- Methods declared in class javax.swing.

JFormattedTextField.AbstractFormatter

getActions

,

getFormattedTextField

,

invalidEdit

,

setEditValid

,

uninstall

- Methods declared in class java.lang.

Object

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

Creates a copy of the DefaultFormatter.

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

Returns when edits are published back to the

JFormattedTextField

.

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

Returns the behavior when inserting characters.

Returns that class that is used to create new Objects.

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).

Sets when edits are published back to the

JFormattedTextField

.

Configures the behavior when inserting characters.

Sets that class that is used to create new Objects.

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument.

Converts the passed in Object into a String by way of the

toString

method.

Methods declared in class javax.swing.

JFormattedTextField.AbstractFormatter

getActions

,

getFormattedTextField

,

invalidEdit

,

setEditValid

,

uninstall

---

#### Methods declared in class javax.swing. JFormattedTextField.AbstractFormatter

Methods declared in class java.lang.

Object

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

- DefaultFormatter

```java
public DefaultFormatter()
```

Creates a DefaultFormatter.

============ METHOD DETAIL ==========

- Method Detail

- install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:** install

in class

JFormattedTextField.AbstractFormatter
**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

- setCommitsOnValidEdit

```java
public void setCommitsOnValidEdit​(boolean commit)
```

Sets when edits are published back to the

JFormattedTextField

. If true,

commitEdit

is invoked after every valid edit (any time the text is edited). On
the other hand, if this is false than the

DefaultFormatter

does not publish edits back to the

JFormattedTextField

.
As such, the only time the value of the

JFormattedTextField

will change is when

commitEdit

is invoked on

JFormattedTextField

, typically when enter is pressed
or focus leaves the

JFormattedTextField

.

**Parameters:** commit

- Used to indicate when edits are committed back to the
JTextComponent

- getCommitsOnValidEdit

```java
public boolean getCommitsOnValidEdit()
```

Returns when edits are published back to the

JFormattedTextField

.

**Returns:** true if edits are committed after every valid edit

- setOverwriteMode

```java
public void setOverwriteMode​(boolean overwriteMode)
```

Configures the behavior when inserting characters. If

overwriteMode

is true (the default), new characters
overwrite existing characters in the model.

**Parameters:** overwriteMode

- Indicates if overwrite or overstrike mode is used

- getOverwriteMode

```java
public boolean getOverwriteMode()
```

Returns the behavior when inserting characters.

**Returns:** true if newly inserted characters overwrite existing characters

- setAllowsInvalid

```java
public void setAllowsInvalid​(boolean allowsInvalid)
```

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).
It is often convenient to allow the user to temporarily input an
invalid value.

**Parameters:** allowsInvalid

- Used to indicate if the edited value must always
be valid

- getAllowsInvalid

```java
public boolean getAllowsInvalid()
```

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

**Returns:** false if the edited value must always be valid

- setValueClass

```java
public void setValueClass​(
Class
<?> valueClass)
```

Sets that class that is used to create new Objects. If the
passed in class does not have a single argument constructor that
takes a String, String values will be used.

**Parameters:** valueClass

- Class used to construct return value from
stringToValue

- getValueClass

```java
public
Class
<?> getValueClass()
```

Returns that class that is used to create new Objects.

**Returns:** Class used to construct return value from stringToValue

- stringToValue

```java
public
Object
stringToValue​(
String
string)
throws
ParseException
```

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument. If

getValueClass

returns null, the Class of the current value in the

JFormattedTextField

will be used. If this is null, a
String will be returned. If the constructor throws an exception, a

ParseException

will be thrown. If there is no single
argument String constructor,

string

will be returned.

**Specified by:** stringToValue

in class

JFormattedTextField.AbstractFormatter
**Parameters:** string

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion

- valueToString

```java
public
String
valueToString​(
Object
value)
throws
ParseException
```

Converts the passed in Object into a String by way of the

toString

method.

**Specified by:** valueToString

in class

JFormattedTextField.AbstractFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

- getDocumentFilter

```java
protected
DocumentFilter
getDocumentFilter()
```

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

**Overrides:** getDocumentFilter

in class

JFormattedTextField.AbstractFormatter
**Returns:** DocumentFilter to restrict edits

- getNavigationFilter

```java
protected
NavigationFilter
getNavigationFilter()
```

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

**Overrides:** getNavigationFilter

in class

JFormattedTextField.AbstractFormatter
**Returns:** NavigationFilter to restrict navigation

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Creates a copy of the DefaultFormatter.

**Overrides:** clone

in class

JFormattedTextField.AbstractFormatter
**Returns:** copy of the DefaultFormatter
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

Constructor Detail

- DefaultFormatter

```java
public DefaultFormatter()
```

Creates a DefaultFormatter.

---

#### Constructor Detail

DefaultFormatter

```java
public DefaultFormatter()
```

Creates a DefaultFormatter.

---

#### DefaultFormatter

public DefaultFormatter()

Creates a DefaultFormatter.

Method Detail

- install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:** install

in class

JFormattedTextField.AbstractFormatter
**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

- setCommitsOnValidEdit

```java
public void setCommitsOnValidEdit​(boolean commit)
```

Sets when edits are published back to the

JFormattedTextField

. If true,

commitEdit

is invoked after every valid edit (any time the text is edited). On
the other hand, if this is false than the

DefaultFormatter

does not publish edits back to the

JFormattedTextField

.
As such, the only time the value of the

JFormattedTextField

will change is when

commitEdit

is invoked on

JFormattedTextField

, typically when enter is pressed
or focus leaves the

JFormattedTextField

.

**Parameters:** commit

- Used to indicate when edits are committed back to the
JTextComponent

- getCommitsOnValidEdit

```java
public boolean getCommitsOnValidEdit()
```

Returns when edits are published back to the

JFormattedTextField

.

**Returns:** true if edits are committed after every valid edit

- setOverwriteMode

```java
public void setOverwriteMode​(boolean overwriteMode)
```

Configures the behavior when inserting characters. If

overwriteMode

is true (the default), new characters
overwrite existing characters in the model.

**Parameters:** overwriteMode

- Indicates if overwrite or overstrike mode is used

- getOverwriteMode

```java
public boolean getOverwriteMode()
```

Returns the behavior when inserting characters.

**Returns:** true if newly inserted characters overwrite existing characters

- setAllowsInvalid

```java
public void setAllowsInvalid​(boolean allowsInvalid)
```

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).
It is often convenient to allow the user to temporarily input an
invalid value.

**Parameters:** allowsInvalid

- Used to indicate if the edited value must always
be valid

- getAllowsInvalid

```java
public boolean getAllowsInvalid()
```

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

**Returns:** false if the edited value must always be valid

- setValueClass

```java
public void setValueClass​(
Class
<?> valueClass)
```

Sets that class that is used to create new Objects. If the
passed in class does not have a single argument constructor that
takes a String, String values will be used.

**Parameters:** valueClass

- Class used to construct return value from
stringToValue

- getValueClass

```java
public
Class
<?> getValueClass()
```

Returns that class that is used to create new Objects.

**Returns:** Class used to construct return value from stringToValue

- stringToValue

```java
public
Object
stringToValue​(
String
string)
throws
ParseException
```

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument. If

getValueClass

returns null, the Class of the current value in the

JFormattedTextField

will be used. If this is null, a
String will be returned. If the constructor throws an exception, a

ParseException

will be thrown. If there is no single
argument String constructor,

string

will be returned.

**Specified by:** stringToValue

in class

JFormattedTextField.AbstractFormatter
**Parameters:** string

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion

- valueToString

```java
public
String
valueToString​(
Object
value)
throws
ParseException
```

Converts the passed in Object into a String by way of the

toString

method.

**Specified by:** valueToString

in class

JFormattedTextField.AbstractFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

- getDocumentFilter

```java
protected
DocumentFilter
getDocumentFilter()
```

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

**Overrides:** getDocumentFilter

in class

JFormattedTextField.AbstractFormatter
**Returns:** DocumentFilter to restrict edits

- getNavigationFilter

```java
protected
NavigationFilter
getNavigationFilter()
```

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

**Overrides:** getNavigationFilter

in class

JFormattedTextField.AbstractFormatter
**Returns:** NavigationFilter to restrict navigation

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Creates a copy of the DefaultFormatter.

**Overrides:** clone

in class

JFormattedTextField.AbstractFormatter
**Returns:** copy of the DefaultFormatter
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

---

#### Method Detail

install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

**Overrides:** install

in class

JFormattedTextField.AbstractFormatter
**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

---

#### install

public void install​(

JFormattedTextField

ftf)

Installs the

DefaultFormatter

onto a particular

JFormattedTextField

.
This will invoke

valueToString

to convert the
current value from the

JFormattedTextField

to
a String. This will then install the

Action

s from

getActions

, the

DocumentFilter

returned from

getDocumentFilter

and the

NavigationFilter

returned from

getNavigationFilter

onto the

JFormattedTextField

.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

Subclasses will typically only need to override this if they
wish to install additional listeners on the

JFormattedTextField

.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

If there is a

ParseException

in converting the
current value to a String, this will set the text to an empty
String, and mark the

JFormattedTextField

as being
in an invalid state.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes.

setCommitsOnValidEdit

```java
public void setCommitsOnValidEdit​(boolean commit)
```

Sets when edits are published back to the

JFormattedTextField

. If true,

commitEdit

is invoked after every valid edit (any time the text is edited). On
the other hand, if this is false than the

DefaultFormatter

does not publish edits back to the

JFormattedTextField

.
As such, the only time the value of the

JFormattedTextField

will change is when

commitEdit

is invoked on

JFormattedTextField

, typically when enter is pressed
or focus leaves the

JFormattedTextField

.

**Parameters:** commit

- Used to indicate when edits are committed back to the
JTextComponent

---

#### setCommitsOnValidEdit

public void setCommitsOnValidEdit​(boolean commit)

Sets when edits are published back to the

JFormattedTextField

. If true,

commitEdit

is invoked after every valid edit (any time the text is edited). On
the other hand, if this is false than the

DefaultFormatter

does not publish edits back to the

JFormattedTextField

.
As such, the only time the value of the

JFormattedTextField

will change is when

commitEdit

is invoked on

JFormattedTextField

, typically when enter is pressed
or focus leaves the

JFormattedTextField

.

getCommitsOnValidEdit

```java
public boolean getCommitsOnValidEdit()
```

Returns when edits are published back to the

JFormattedTextField

.

**Returns:** true if edits are committed after every valid edit

---

#### getCommitsOnValidEdit

public boolean getCommitsOnValidEdit()

Returns when edits are published back to the

JFormattedTextField

.

setOverwriteMode

```java
public void setOverwriteMode​(boolean overwriteMode)
```

Configures the behavior when inserting characters. If

overwriteMode

is true (the default), new characters
overwrite existing characters in the model.

**Parameters:** overwriteMode

- Indicates if overwrite or overstrike mode is used

---

#### setOverwriteMode

public void setOverwriteMode​(boolean overwriteMode)

Configures the behavior when inserting characters. If

overwriteMode

is true (the default), new characters
overwrite existing characters in the model.

getOverwriteMode

```java
public boolean getOverwriteMode()
```

Returns the behavior when inserting characters.

**Returns:** true if newly inserted characters overwrite existing characters

---

#### getOverwriteMode

public boolean getOverwriteMode()

Returns the behavior when inserting characters.

setAllowsInvalid

```java
public void setAllowsInvalid​(boolean allowsInvalid)
```

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).
It is often convenient to allow the user to temporarily input an
invalid value.

**Parameters:** allowsInvalid

- Used to indicate if the edited value must always
be valid

---

#### setAllowsInvalid

public void setAllowsInvalid​(boolean allowsInvalid)

Sets whether or not the value being edited is allowed to be invalid
for a length of time (that is,

stringToValue

throws
a

ParseException

).
It is often convenient to allow the user to temporarily input an
invalid value.

getAllowsInvalid

```java
public boolean getAllowsInvalid()
```

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

**Returns:** false if the edited value must always be valid

---

#### getAllowsInvalid

public boolean getAllowsInvalid()

Returns whether or not the value being edited is allowed to be invalid
for a length of time.

setValueClass

```java
public void setValueClass​(
Class
<?> valueClass)
```

Sets that class that is used to create new Objects. If the
passed in class does not have a single argument constructor that
takes a String, String values will be used.

**Parameters:** valueClass

- Class used to construct return value from
stringToValue

---

#### setValueClass

public void setValueClass​(

Class

<?> valueClass)

Sets that class that is used to create new Objects. If the
passed in class does not have a single argument constructor that
takes a String, String values will be used.

getValueClass

```java
public
Class
<?> getValueClass()
```

Returns that class that is used to create new Objects.

**Returns:** Class used to construct return value from stringToValue

---

#### getValueClass

public

Class

<?> getValueClass()

Returns that class that is used to create new Objects.

stringToValue

```java
public
Object
stringToValue​(
String
string)
throws
ParseException
```

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument. If

getValueClass

returns null, the Class of the current value in the

JFormattedTextField

will be used. If this is null, a
String will be returned. If the constructor throws an exception, a

ParseException

will be thrown. If there is no single
argument String constructor,

string

will be returned.

**Specified by:** stringToValue

in class

JFormattedTextField.AbstractFormatter
**Parameters:** string

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion

---

#### stringToValue

public

Object

stringToValue​(

String

string)
throws

ParseException

Converts the passed in String into an instance of

getValueClass

by way of the constructor that
takes a String argument. If

getValueClass

returns null, the Class of the current value in the

JFormattedTextField

will be used. If this is null, a
String will be returned. If the constructor throws an exception, a

ParseException

will be thrown. If there is no single
argument String constructor,

string

will be returned.

valueToString

```java
public
String
valueToString​(
Object
value)
throws
ParseException
```

Converts the passed in Object into a String by way of the

toString

method.

**Specified by:** valueToString

in class

JFormattedTextField.AbstractFormatter
**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

---

#### valueToString

public

String

valueToString​(

Object

value)
throws

ParseException

Converts the passed in Object into a String by way of the

toString

method.

getDocumentFilter

```java
protected
DocumentFilter
getDocumentFilter()
```

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

**Overrides:** getDocumentFilter

in class

JFormattedTextField.AbstractFormatter
**Returns:** DocumentFilter to restrict edits

---

#### getDocumentFilter

protected

DocumentFilter

getDocumentFilter()

Returns the

DocumentFilter

used to restrict the characters
that can be input into the

JFormattedTextField

.

getNavigationFilter

```java
protected
NavigationFilter
getNavigationFilter()
```

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

**Overrides:** getNavigationFilter

in class

JFormattedTextField.AbstractFormatter
**Returns:** NavigationFilter to restrict navigation

---

#### getNavigationFilter

protected

NavigationFilter

getNavigationFilter()

Returns the

NavigationFilter

used to restrict where the
cursor can be placed.

clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Creates a copy of the DefaultFormatter.

**Overrides:** clone

in class

JFormattedTextField.AbstractFormatter
**Returns:** copy of the DefaultFormatter
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

---

#### clone

public

Object

clone()
throws

CloneNotSupportedException

Creates a copy of the DefaultFormatter.

---

