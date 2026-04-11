# Class Option

**Source:** `java.desktop\javax\swing\text\html\Option.html`

### Class Description

```java
public class
Option

extends
Object

implements
Serializable
```

Value for the ListModel used to represent
<option> elements. This is the object
installed as items of the DefaultComboBoxModel
used to represent the <select> element.

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

#### public Option​(
AttributeSet
attr)

Creates a new Option object.

**Parameters:**
- attr

- the attributes associated with the
option element. The attributes are copied to
ensure they won't change.

---

### Method Details

#### public void setLabel​(
String
label)

Sets the label to be used for the option.

**Parameters:**
- label

- a label.

---

#### public
String
getLabel()

Fetch the label associated with the option.

**Returns:**
- the label associated with the option.

---

#### public
AttributeSet
getAttributes()

Fetch the attributes associated with this option.

**Returns:**
- the attributes associated with this option.

---

#### public
String
toString()

String representation is the label.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### protected void setSelection​(boolean state)

Sets the selected state.

**Parameters:**
- state

- a selection state

---

#### public boolean isSelected()

Fetches the selection state associated with this option.

**Returns:**
- the selection state.

---

#### public
String
getValue()

Convenient method to return the string associated
with the

value

attribute. If the

value

has not been specified, the

label

will be
returned.

**Returns:**
- the string associated with the

value

attribute,
or

label

if the value has been not specified.

---

### Additional Sections

#### Class Option

java.lang.Object

- javax.swing.text.html.Option

javax.swing.text.html.Option

**All Implemented Interfaces:** Serializable

```java
public class
Option

extends
Object

implements
Serializable
```

Value for the ListModel used to represent
<option> elements. This is the object
installed as items of the DefaultComboBoxModel
used to represent the <select> element.

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

**See Also:** Serialized Form

public class

Option

extends

Object

implements

Serializable

Value for the ListModel used to represent
<option> elements. This is the object
installed as items of the DefaultComboBoxModel
used to represent the <select> element.

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

Option

​(

AttributeSet

attr)

Creates a new Option object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AttributeSet

getAttributes

()

Fetch the attributes associated with this option.

String

getLabel

()

Fetch the label associated with the option.

String

getValue

()

Convenient method to return the string associated
with the

value

attribute.

boolean

isSelected

()

Fetches the selection state associated with this option.

void

setLabel

​(

String

label)

Sets the label to be used for the option.

protected void

setSelection

​(boolean state)

Sets the selected state.

String

toString

()

String representation is the label.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

Option

​(

AttributeSet

attr)

Creates a new Option object.

---

#### Constructor Summary

Creates a new Option object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AttributeSet

getAttributes

()

Fetch the attributes associated with this option.

String

getLabel

()

Fetch the label associated with the option.

String

getValue

()

Convenient method to return the string associated
with the

value

attribute.

boolean

isSelected

()

Fetches the selection state associated with this option.

void

setLabel

​(

String

label)

Sets the label to be used for the option.

protected void

setSelection

​(boolean state)

Sets the selected state.

String

toString

()

String representation is the label.

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

wait

,

wait

,

wait

---

#### Method Summary

Fetch the attributes associated with this option.

Fetch the label associated with the option.

Convenient method to return the string associated
with the

value

attribute.

Fetches the selection state associated with this option.

Sets the label to be used for the option.

Sets the selected state.

String representation is the label.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Option

```java
public Option​(
AttributeSet
attr)
```

Creates a new Option object.

**Parameters:** attr

- the attributes associated with the
option element. The attributes are copied to
ensure they won't change.

============ METHOD DETAIL ==========

- Method Detail

- setLabel

```java
public void setLabel​(
String
label)
```

Sets the label to be used for the option.

**Parameters:** label

- a label.

- getLabel

```java
public
String
getLabel()
```

Fetch the label associated with the option.

**Returns:** the label associated with the option.

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetch the attributes associated with this option.

**Returns:** the attributes associated with this option.

- toString

```java
public
String
toString()
```

String representation is the label.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- setSelection

```java
protected void setSelection​(boolean state)
```

Sets the selected state.

**Parameters:** state

- a selection state

- isSelected

```java
public boolean isSelected()
```

Fetches the selection state associated with this option.

**Returns:** the selection state.

- getValue

```java
public
String
getValue()
```

Convenient method to return the string associated
with the

value

attribute. If the

value

has not been specified, the

label

will be
returned.

**Returns:** the string associated with the

value

attribute,
or

label

if the value has been not specified.

Constructor Detail

- Option

```java
public Option​(
AttributeSet
attr)
```

Creates a new Option object.

**Parameters:** attr

- the attributes associated with the
option element. The attributes are copied to
ensure they won't change.

---

#### Constructor Detail

Option

```java
public Option​(
AttributeSet
attr)
```

Creates a new Option object.

**Parameters:** attr

- the attributes associated with the
option element. The attributes are copied to
ensure they won't change.

---

#### Option

public Option​(

AttributeSet

attr)

Creates a new Option object.

Method Detail

- setLabel

```java
public void setLabel​(
String
label)
```

Sets the label to be used for the option.

**Parameters:** label

- a label.

- getLabel

```java
public
String
getLabel()
```

Fetch the label associated with the option.

**Returns:** the label associated with the option.

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetch the attributes associated with this option.

**Returns:** the attributes associated with this option.

- toString

```java
public
String
toString()
```

String representation is the label.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- setSelection

```java
protected void setSelection​(boolean state)
```

Sets the selected state.

**Parameters:** state

- a selection state

- isSelected

```java
public boolean isSelected()
```

Fetches the selection state associated with this option.

**Returns:** the selection state.

- getValue

```java
public
String
getValue()
```

Convenient method to return the string associated
with the

value

attribute. If the

value

has not been specified, the

label

will be
returned.

**Returns:** the string associated with the

value

attribute,
or

label

if the value has been not specified.

---

#### Method Detail

setLabel

```java
public void setLabel​(
String
label)
```

Sets the label to be used for the option.

**Parameters:** label

- a label.

---

#### setLabel

public void setLabel​(

String

label)

Sets the label to be used for the option.

getLabel

```java
public
String
getLabel()
```

Fetch the label associated with the option.

**Returns:** the label associated with the option.

---

#### getLabel

public

String

getLabel()

Fetch the label associated with the option.

getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetch the attributes associated with this option.

**Returns:** the attributes associated with this option.

---

#### getAttributes

public

AttributeSet

getAttributes()

Fetch the attributes associated with this option.

toString

```java
public
String
toString()
```

String representation is the label.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

String representation is the label.

setSelection

```java
protected void setSelection​(boolean state)
```

Sets the selected state.

**Parameters:** state

- a selection state

---

#### setSelection

protected void setSelection​(boolean state)

Sets the selected state.

isSelected

```java
public boolean isSelected()
```

Fetches the selection state associated with this option.

**Returns:** the selection state.

---

#### isSelected

public boolean isSelected()

Fetches the selection state associated with this option.

getValue

```java
public
String
getValue()
```

Convenient method to return the string associated
with the

value

attribute. If the

value

has not been specified, the

label

will be
returned.

**Returns:** the string associated with the

value

attribute,
or

label

if the value has been not specified.

---

#### getValue

public

String

getValue()

Convenient method to return the string associated
with the

value

attribute. If the

value

has not been specified, the

label

will be
returned.

---

