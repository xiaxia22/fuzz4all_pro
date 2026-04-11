# Class JFormattedTextField.AbstractFormatter

**Source:** `java.desktop\javax\swing\JFormattedTextField.AbstractFormatter.html`

### Class Description

```java
public abstract static class
JFormattedTextField.AbstractFormatter

extends
Object

implements
Serializable
```

Instances of

AbstractFormatter

are used by

JFormattedTextField

to handle the conversion both
from an Object to a String, and back from a String to an Object.

AbstractFormatter

s can also enforce editing policies,
or navigation policies, or manipulate the

JFormattedTextField

in any way it sees fit to
enforce the desired policy.

An

AbstractFormatter

can only be active in
one

JFormattedTextField

at a time.

JFormattedTextField

invokes

install

when it is ready to use it followed
by

uninstall

when done. Subclasses
that wish to install additional state should override

install

and message super appropriately.

Subclasses must override the conversion methods

stringToValue

and

valueToString

. Optionally
they can override

getActions

,

getNavigationFilter

and

getDocumentFilter

to restrict the

JFormattedTextField

in a particular
way.

Subclasses that allow the

JFormattedTextField

to be in
a temporarily invalid state should invoke

setEditValid

at the appropriate times.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AbstractFormatter()

*No description found.*

---

### Method Details

#### public void install​(
JFormattedTextField
ftf)

Installs the

AbstractFormatter

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
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

**Parameters:**
- ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

---

#### public void uninstall()

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

. This resets the

DocumentFilter

,

NavigationFilter

and additional

Action

s installed on the

JFormattedTextField

.

---

#### public abstract
Object
stringToValue​(
String
text)
throws
ParseException

Parses

text

returning an arbitrary Object. Some
formatters may return null.

**Parameters:**
- text

- String to convert

**Returns:**
- Object representation of text

**Throws:**
- ParseException

- if there is an error in the conversion

---

#### public abstract
String
valueToString​(
Object
value)
throws
ParseException

Returns the string value to display for

value

.

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
JFormattedTextField
getFormattedTextField()

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

**Returns:**
- JFormattedTextField formatting for.

---

#### protected void invalidEdit()

This should be invoked when the user types an invalid character.
This forwards the call to the current JFormattedTextField.

---

#### protected void setEditValid​(boolean valid)

Invoke this to update the

editValid

property of the

JFormattedTextField

. If you an enforce a policy
such that the

JFormattedTextField

is always in a
valid state, you will never need to invoke this.

**Parameters:**
- valid

- Valid state of the JFormattedTextField

---

#### protected
Action
[] getActions()

Subclass and override if you wish to provide a custom set of

Action

s.

install

will install these
on the

JFormattedTextField

's

ActionMap

.

**Returns:**
- Array of Actions to install on JFormattedTextField

---

#### protected
DocumentFilter
getDocumentFilter()

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:**
- DocumentFilter to restrict edits

---

#### protected
NavigationFilter
getNavigationFilter()

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:**
- NavigationFilter to restrict navigation

---

#### protected
Object
clone()
throws
CloneNotSupportedException

Clones the

AbstractFormatter

. The returned instance
is not associated with a

JFormattedTextField

.

**Overrides:**
- clone

in class

Object

**Returns:**
- Copy of the AbstractFormatter

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

#### Class JFormattedTextField.AbstractFormatter

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatter

javax.swing.JFormattedTextField.AbstractFormatter

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** DefaultFormatter

**Enclosing class:** JFormattedTextField

```java
public abstract static class
JFormattedTextField.AbstractFormatter

extends
Object

implements
Serializable
```

Instances of

AbstractFormatter

are used by

JFormattedTextField

to handle the conversion both
from an Object to a String, and back from a String to an Object.

AbstractFormatter

s can also enforce editing policies,
or navigation policies, or manipulate the

JFormattedTextField

in any way it sees fit to
enforce the desired policy.

An

AbstractFormatter

can only be active in
one

JFormattedTextField

at a time.

JFormattedTextField

invokes

install

when it is ready to use it followed
by

uninstall

when done. Subclasses
that wish to install additional state should override

install

and message super appropriately.

Subclasses must override the conversion methods

stringToValue

and

valueToString

. Optionally
they can override

getActions

,

getNavigationFilter

and

getDocumentFilter

to restrict the

JFormattedTextField

in a particular
way.

Subclasses that allow the

JFormattedTextField

to be in
a temporarily invalid state should invoke

setEditValid

at the appropriate times.

**Since:** 1.4
**See Also:** Serialized Form

public abstract static class

JFormattedTextField.AbstractFormatter

extends

Object

implements

Serializable

Instances of

AbstractFormatter

are used by

JFormattedTextField

to handle the conversion both
from an Object to a String, and back from a String to an Object.

AbstractFormatter

s can also enforce editing policies,
or navigation policies, or manipulate the

JFormattedTextField

in any way it sees fit to
enforce the desired policy.

An

AbstractFormatter

can only be active in
one

JFormattedTextField

at a time.

JFormattedTextField

invokes

install

when it is ready to use it followed
by

uninstall

when done. Subclasses
that wish to install additional state should override

install

and message super appropriately.

Subclasses must override the conversion methods

stringToValue

and

valueToString

. Optionally
they can override

getActions

,

getNavigationFilter

and

getDocumentFilter

to restrict the

JFormattedTextField

in a particular
way.

Subclasses that allow the

JFormattedTextField

to be in
a temporarily invalid state should invoke

setEditValid

at the appropriate times.

An

AbstractFormatter

can only be active in
one

JFormattedTextField

at a time.

JFormattedTextField

invokes

install

when it is ready to use it followed
by

uninstall

when done. Subclasses
that wish to install additional state should override

install

and message super appropriately.

Subclasses must override the conversion methods

stringToValue

and

valueToString

. Optionally
they can override

getActions

,

getNavigationFilter

and

getDocumentFilter

to restrict the

JFormattedTextField

in a particular
way.

Subclasses that allow the

JFormattedTextField

to be in
a temporarily invalid state should invoke

setEditValid

at the appropriate times.

Subclasses must override the conversion methods

stringToValue

and

valueToString

. Optionally
they can override

getActions

,

getNavigationFilter

and

getDocumentFilter

to restrict the

JFormattedTextField

in a particular
way.

Subclasses that allow the

JFormattedTextField

to be in
a temporarily invalid state should invoke

setEditValid

at the appropriate times.

Subclasses that allow the

JFormattedTextField

to be in
a temporarily invalid state should invoke

setEditValid

at the appropriate times.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractFormatter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

clone

()

Clones the

AbstractFormatter

.

protected

Action

[]

getActions

()

Subclass and override if you wish to provide a custom set of

Action

s.

protected

DocumentFilter

getDocumentFilter

()

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

protected

JFormattedTextField

getFormattedTextField

()

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

protected

NavigationFilter

getNavigationFilter

()

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

void

install

​(

JFormattedTextField

ftf)

Installs the

AbstractFormatter

onto a particular

JFormattedTextField

.

protected void

invalidEdit

()

This should be invoked when the user types an invalid character.

protected void

setEditValid

​(boolean valid)

Invoke this to update the

editValid

property of the

JFormattedTextField

.

abstract

Object

stringToValue

​(

String

text)

Parses

text

returning an arbitrary Object.

void

uninstall

()

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

.

abstract

String

valueToString

​(

Object

value)

Returns the string value to display for

value

.

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

AbstractFormatter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

clone

()

Clones the

AbstractFormatter

.

protected

Action

[]

getActions

()

Subclass and override if you wish to provide a custom set of

Action

s.

protected

DocumentFilter

getDocumentFilter

()

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

protected

JFormattedTextField

getFormattedTextField

()

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

protected

NavigationFilter

getNavigationFilter

()

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

void

install

​(

JFormattedTextField

ftf)

Installs the

AbstractFormatter

onto a particular

JFormattedTextField

.

protected void

invalidEdit

()

This should be invoked when the user types an invalid character.

protected void

setEditValid

​(boolean valid)

Invoke this to update the

editValid

property of the

JFormattedTextField

.

abstract

Object

stringToValue

​(

String

text)

Parses

text

returning an arbitrary Object.

void

uninstall

()

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

.

abstract

String

valueToString

​(

Object

value)

Returns the string value to display for

value

.

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

Clones the

AbstractFormatter

.

Subclass and override if you wish to provide a custom set of

Action

s.

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

Installs the

AbstractFormatter

onto a particular

JFormattedTextField

.

This should be invoked when the user types an invalid character.

Invoke this to update the

editValid

property of the

JFormattedTextField

.

Parses

text

returning an arbitrary Object.

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

.

Returns the string value to display for

value

.

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

- AbstractFormatter

```java
public AbstractFormatter()
```

============ METHOD DETAIL ==========

- Method Detail

- install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

AbstractFormatter

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
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

- uninstall

```java
public void uninstall()
```

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

. This resets the

DocumentFilter

,

NavigationFilter

and additional

Action

s installed on the

JFormattedTextField

.

- stringToValue

```java
public abstract
Object
stringToValue​(
String
text)
throws
ParseException
```

Parses

text

returning an arbitrary Object. Some
formatters may return null.

**Parameters:** text

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion

- valueToString

```java
public abstract
String
valueToString​(
Object
value)
throws
ParseException
```

Returns the string value to display for

value

.

**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

- getFormattedTextField

```java
protected
JFormattedTextField
getFormattedTextField()
```

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

**Returns:** JFormattedTextField formatting for.

- invalidEdit

```java
protected void invalidEdit()
```

This should be invoked when the user types an invalid character.
This forwards the call to the current JFormattedTextField.

- setEditValid

```java
protected void setEditValid​(boolean valid)
```

Invoke this to update the

editValid

property of the

JFormattedTextField

. If you an enforce a policy
such that the

JFormattedTextField

is always in a
valid state, you will never need to invoke this.

**Parameters:** valid

- Valid state of the JFormattedTextField

- getActions

```java
protected
Action
[] getActions()
```

Subclass and override if you wish to provide a custom set of

Action

s.

install

will install these
on the

JFormattedTextField

's

ActionMap

.

**Returns:** Array of Actions to install on JFormattedTextField

- getDocumentFilter

```java
protected
DocumentFilter
getDocumentFilter()
```

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:** DocumentFilter to restrict edits

- getNavigationFilter

```java
protected
NavigationFilter
getNavigationFilter()
```

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:** NavigationFilter to restrict navigation

- clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Clones the

AbstractFormatter

. The returned instance
is not associated with a

JFormattedTextField

.

**Overrides:** clone

in class

Object
**Returns:** Copy of the AbstractFormatter
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

- AbstractFormatter

```java
public AbstractFormatter()
```

---

#### Constructor Detail

AbstractFormatter

```java
public AbstractFormatter()
```

---

#### AbstractFormatter

public AbstractFormatter()

Method Detail

- install

```java
public void install​(
JFormattedTextField
ftf)
```

Installs the

AbstractFormatter

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
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

- uninstall

```java
public void uninstall()
```

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

. This resets the

DocumentFilter

,

NavigationFilter

and additional

Action

s installed on the

JFormattedTextField

.

- stringToValue

```java
public abstract
Object
stringToValue​(
String
text)
throws
ParseException
```

Parses

text

returning an arbitrary Object. Some
formatters may return null.

**Parameters:** text

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion

- valueToString

```java
public abstract
String
valueToString​(
Object
value)
throws
ParseException
```

Returns the string value to display for

value

.

**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

- getFormattedTextField

```java
protected
JFormattedTextField
getFormattedTextField()
```

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

**Returns:** JFormattedTextField formatting for.

- invalidEdit

```java
protected void invalidEdit()
```

This should be invoked when the user types an invalid character.
This forwards the call to the current JFormattedTextField.

- setEditValid

```java
protected void setEditValid​(boolean valid)
```

Invoke this to update the

editValid

property of the

JFormattedTextField

. If you an enforce a policy
such that the

JFormattedTextField

is always in a
valid state, you will never need to invoke this.

**Parameters:** valid

- Valid state of the JFormattedTextField

- getActions

```java
protected
Action
[] getActions()
```

Subclass and override if you wish to provide a custom set of

Action

s.

install

will install these
on the

JFormattedTextField

's

ActionMap

.

**Returns:** Array of Actions to install on JFormattedTextField

- getDocumentFilter

```java
protected
DocumentFilter
getDocumentFilter()
```

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:** DocumentFilter to restrict edits

- getNavigationFilter

```java
protected
NavigationFilter
getNavigationFilter()
```

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:** NavigationFilter to restrict navigation

- clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Clones the

AbstractFormatter

. The returned instance
is not associated with a

JFormattedTextField

.

**Overrides:** clone

in class

Object
**Returns:** Copy of the AbstractFormatter
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

AbstractFormatter

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
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

**Parameters:** ftf

- JFormattedTextField to format for, may be null indicating
uninstall from current JFormattedTextField.

---

#### install

public void install​(

JFormattedTextField

ftf)

Installs the

AbstractFormatter

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
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

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
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

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
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

While this is a public method, this is typically only useful
for subclassers of

JFormattedTextField

.

JFormattedTextField

will invoke this method at
the appropriate times when the value changes, or its internal
state changes. You will only need to invoke this yourself if
you are subclassing

JFormattedTextField

and
installing/uninstalling

AbstractFormatter

at a
different time than

JFormattedTextField

does.

uninstall

```java
public void uninstall()
```

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

. This resets the

DocumentFilter

,

NavigationFilter

and additional

Action

s installed on the

JFormattedTextField

.

---

#### uninstall

public void uninstall()

Uninstalls any state the

AbstractFormatter

may have
installed on the

JFormattedTextField

. This resets the

DocumentFilter

,

NavigationFilter

and additional

Action

s installed on the

JFormattedTextField

.

stringToValue

```java
public abstract
Object
stringToValue​(
String
text)
throws
ParseException
```

Parses

text

returning an arbitrary Object. Some
formatters may return null.

**Parameters:** text

- String to convert
**Returns:** Object representation of text
**Throws:** ParseException

- if there is an error in the conversion

---

#### stringToValue

public abstract

Object

stringToValue​(

String

text)
throws

ParseException

Parses

text

returning an arbitrary Object. Some
formatters may return null.

valueToString

```java
public abstract
String
valueToString​(
Object
value)
throws
ParseException
```

Returns the string value to display for

value

.

**Parameters:** value

- Value to convert
**Returns:** String representation of value
**Throws:** ParseException

- if there is an error in the conversion

---

#### valueToString

public abstract

String

valueToString​(

Object

value)
throws

ParseException

Returns the string value to display for

value

.

getFormattedTextField

```java
protected
JFormattedTextField
getFormattedTextField()
```

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

**Returns:** JFormattedTextField formatting for.

---

#### getFormattedTextField

protected

JFormattedTextField

getFormattedTextField()

Returns the current

JFormattedTextField

the

AbstractFormatter

is installed on.

invalidEdit

```java
protected void invalidEdit()
```

This should be invoked when the user types an invalid character.
This forwards the call to the current JFormattedTextField.

---

#### invalidEdit

protected void invalidEdit()

This should be invoked when the user types an invalid character.
This forwards the call to the current JFormattedTextField.

setEditValid

```java
protected void setEditValid​(boolean valid)
```

Invoke this to update the

editValid

property of the

JFormattedTextField

. If you an enforce a policy
such that the

JFormattedTextField

is always in a
valid state, you will never need to invoke this.

**Parameters:** valid

- Valid state of the JFormattedTextField

---

#### setEditValid

protected void setEditValid​(boolean valid)

Invoke this to update the

editValid

property of the

JFormattedTextField

. If you an enforce a policy
such that the

JFormattedTextField

is always in a
valid state, you will never need to invoke this.

getActions

```java
protected
Action
[] getActions()
```

Subclass and override if you wish to provide a custom set of

Action

s.

install

will install these
on the

JFormattedTextField

's

ActionMap

.

**Returns:** Array of Actions to install on JFormattedTextField

---

#### getActions

protected

Action

[] getActions()

Subclass and override if you wish to provide a custom set of

Action

s.

install

will install these
on the

JFormattedTextField

's

ActionMap

.

getDocumentFilter

```java
protected
DocumentFilter
getDocumentFilter()
```

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:** DocumentFilter to restrict edits

---

#### getDocumentFilter

protected

DocumentFilter

getDocumentFilter()

Subclass and override if you wish to provide a

DocumentFilter

to restrict what can be input.

install

will install the returned value onto
the

JFormattedTextField

.

getNavigationFilter

```java
protected
NavigationFilter
getNavigationFilter()
```

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

install

will install the returned value onto
the

JFormattedTextField

.

**Returns:** NavigationFilter to restrict navigation

---

#### getNavigationFilter

protected

NavigationFilter

getNavigationFilter()

Subclass and override if you wish to provide a filter to restrict
where the user can navigate to.

install

will install the returned value onto
the

JFormattedTextField

.

clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Clones the

AbstractFormatter

. The returned instance
is not associated with a

JFormattedTextField

.

**Overrides:** clone

in class

Object
**Returns:** Copy of the AbstractFormatter
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

protected

Object

clone()
throws

CloneNotSupportedException

Clones the

AbstractFormatter

. The returned instance
is not associated with a

JFormattedTextField

.

---

