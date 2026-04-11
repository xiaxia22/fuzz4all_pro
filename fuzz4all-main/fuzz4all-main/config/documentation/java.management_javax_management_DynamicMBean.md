# Interface DynamicMBean

**Source:** `java.management\javax\management\DynamicMBean.html`

### Class Description

```java
public interface
DynamicMBean
```

Defines the methods that should be implemented by
a Dynamic MBean (MBean that exposes a dynamic management interface).

**All Known Subinterfaces:** DiagnosticCommandMBean

,

ModelMBean

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
getAttribute​(
String
attribute)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException

Obtain the value of a specific attribute of the Dynamic MBean.

**Parameters:**
- attribute

- The name of the attribute to be retrieved

**Returns:**
- The value of the attribute retrieved.

**Throws:**
- AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
- MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's getter.
- ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the getter.

**See Also:**
- setAttribute(javax.management.Attribute)

---

#### void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException

Set the value of a specific attribute of the Dynamic MBean.

**Parameters:**
- attribute

- The identification of the attribute to
be set and the value it is to be set to.

**Throws:**
- AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
- InvalidAttributeValueException

- if value specified is not valid for the attribute
- MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's setter.
- ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the MBean's setter.

**See Also:**
- getAttribute(java.lang.String)

---

#### AttributeList
getAttributes​(
String
[] attributes)

Get the values of several attributes of the Dynamic MBean.

**Parameters:**
- attributes

- A list of the attributes to be retrieved.

**Returns:**
- The list of attributes retrieved.

**See Also:**
- setAttributes(javax.management.AttributeList)

---

#### AttributeList
setAttributes​(
AttributeList
attributes)

Sets the values of several attributes of the Dynamic MBean.

**Parameters:**
- attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.

**Returns:**
- The list of attributes that were set, with their new values.

**See Also:**
- getAttributes(java.lang.String[])

---

#### Object
invoke​(
String
actionName,

Object
[] params,

String
[] signature)
throws
MBeanException
,

ReflectionException

Allows an action to be invoked on the Dynamic MBean.

**Parameters:**
- actionName

- The name of the action to be invoked.
- params

- An array containing the parameters to be set when the action is
invoked.
- signature

- An array containing the signature of the action. The class objects will
be loaded through the same class loader as the one used for loading the
MBean on which the action is invoked.

**Returns:**
- The object returned by the action, which represents the result of
invoking the action on the MBean specified.

**Throws:**
- MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's invoked method.
- ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the method

---

#### MBeanInfo
getMBeanInfo()

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

**Returns:**
- An instance of

MBeanInfo

allowing all attributes and actions
exposed by this Dynamic MBean to be retrieved.

---

### Additional Sections

#### Interface DynamicMBean

**All Known Subinterfaces:** DiagnosticCommandMBean

,

ModelMBean

**All Known Implementing Classes:** RequiredModelMBean

,

StandardEmitterMBean

,

StandardMBean

```java
public interface
DynamicMBean
```

Defines the methods that should be implemented by
a Dynamic MBean (MBean that exposes a dynamic management interface).

**Since:** 1.5

public interface

DynamicMBean

Defines the methods that should be implemented by
a Dynamic MBean (MBean that exposes a dynamic management interface).

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

attribute)

Obtain the value of a specific attribute of the Dynamic MBean.

AttributeList

getAttributes

​(

String

[] attributes)

Get the values of several attributes of the Dynamic MBean.

MBeanInfo

getMBeanInfo

()

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

Object

invoke

​(

String

actionName,

Object

[] params,

String

[] signature)

Allows an action to be invoked on the Dynamic MBean.

void

setAttribute

​(

Attribute

attribute)

Set the value of a specific attribute of the Dynamic MBean.

AttributeList

setAttributes

​(

AttributeList

attributes)

Sets the values of several attributes of the Dynamic MBean.

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

attribute)

Obtain the value of a specific attribute of the Dynamic MBean.

AttributeList

getAttributes

​(

String

[] attributes)

Get the values of several attributes of the Dynamic MBean.

MBeanInfo

getMBeanInfo

()

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

Object

invoke

​(

String

actionName,

Object

[] params,

String

[] signature)

Allows an action to be invoked on the Dynamic MBean.

void

setAttribute

​(

Attribute

attribute)

Set the value of a specific attribute of the Dynamic MBean.

AttributeList

setAttributes

​(

AttributeList

attributes)

Sets the values of several attributes of the Dynamic MBean.

---

#### Method Summary

Obtain the value of a specific attribute of the Dynamic MBean.

Get the values of several attributes of the Dynamic MBean.

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

Allows an action to be invoked on the Dynamic MBean.

Set the value of a specific attribute of the Dynamic MBean.

Sets the values of several attributes of the Dynamic MBean.

============ METHOD DETAIL ==========

- Method Detail

- getAttribute

```java
Object
getAttribute​(
String
attribute)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException
```

Obtain the value of a specific attribute of the Dynamic MBean.

**Parameters:** attribute

- The name of the attribute to be retrieved
**Returns:** The value of the attribute retrieved.
**Throws:** AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's getter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the getter.
**See Also:** setAttribute(javax.management.Attribute)

- setAttribute

```java
void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
```

Set the value of a specific attribute of the Dynamic MBean.

**Parameters:** attribute

- The identification of the attribute to
be set and the value it is to be set to.
**Throws:** AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
**Throws:** InvalidAttributeValueException

- if value specified is not valid for the attribute
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's setter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the MBean's setter.
**See Also:** getAttribute(java.lang.String)

- getAttributes

```java
AttributeList
getAttributes​(
String
[] attributes)
```

Get the values of several attributes of the Dynamic MBean.

**Parameters:** attributes

- A list of the attributes to be retrieved.
**Returns:** The list of attributes retrieved.
**See Also:** setAttributes(javax.management.AttributeList)

- setAttributes

```java
AttributeList
setAttributes​(
AttributeList
attributes)
```

Sets the values of several attributes of the Dynamic MBean.

**Parameters:** attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.
**Returns:** The list of attributes that were set, with their new values.
**See Also:** getAttributes(java.lang.String[])

- invoke

```java
Object
invoke​(
String
actionName,

Object
[] params,

String
[] signature)
throws
MBeanException
,

ReflectionException
```

Allows an action to be invoked on the Dynamic MBean.

**Parameters:** actionName

- The name of the action to be invoked.
**Parameters:** params

- An array containing the parameters to be set when the action is
invoked.
**Parameters:** signature

- An array containing the signature of the action. The class objects will
be loaded through the same class loader as the one used for loading the
MBean on which the action is invoked.
**Returns:** The object returned by the action, which represents the result of
invoking the action on the MBean specified.
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's invoked method.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the method

- getMBeanInfo

```java
MBeanInfo
getMBeanInfo()
```

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

**Returns:** An instance of

MBeanInfo

allowing all attributes and actions
exposed by this Dynamic MBean to be retrieved.

Method Detail

- getAttribute

```java
Object
getAttribute​(
String
attribute)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException
```

Obtain the value of a specific attribute of the Dynamic MBean.

**Parameters:** attribute

- The name of the attribute to be retrieved
**Returns:** The value of the attribute retrieved.
**Throws:** AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's getter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the getter.
**See Also:** setAttribute(javax.management.Attribute)

- setAttribute

```java
void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
```

Set the value of a specific attribute of the Dynamic MBean.

**Parameters:** attribute

- The identification of the attribute to
be set and the value it is to be set to.
**Throws:** AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
**Throws:** InvalidAttributeValueException

- if value specified is not valid for the attribute
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's setter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the MBean's setter.
**See Also:** getAttribute(java.lang.String)

- getAttributes

```java
AttributeList
getAttributes​(
String
[] attributes)
```

Get the values of several attributes of the Dynamic MBean.

**Parameters:** attributes

- A list of the attributes to be retrieved.
**Returns:** The list of attributes retrieved.
**See Also:** setAttributes(javax.management.AttributeList)

- setAttributes

```java
AttributeList
setAttributes​(
AttributeList
attributes)
```

Sets the values of several attributes of the Dynamic MBean.

**Parameters:** attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.
**Returns:** The list of attributes that were set, with their new values.
**See Also:** getAttributes(java.lang.String[])

- invoke

```java
Object
invoke​(
String
actionName,

Object
[] params,

String
[] signature)
throws
MBeanException
,

ReflectionException
```

Allows an action to be invoked on the Dynamic MBean.

**Parameters:** actionName

- The name of the action to be invoked.
**Parameters:** params

- An array containing the parameters to be set when the action is
invoked.
**Parameters:** signature

- An array containing the signature of the action. The class objects will
be loaded through the same class loader as the one used for loading the
MBean on which the action is invoked.
**Returns:** The object returned by the action, which represents the result of
invoking the action on the MBean specified.
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's invoked method.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the method

- getMBeanInfo

```java
MBeanInfo
getMBeanInfo()
```

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

**Returns:** An instance of

MBeanInfo

allowing all attributes and actions
exposed by this Dynamic MBean to be retrieved.

---

#### Method Detail

getAttribute

```java
Object
getAttribute​(
String
attribute)
throws
AttributeNotFoundException
,

MBeanException
,

ReflectionException
```

Obtain the value of a specific attribute of the Dynamic MBean.

**Parameters:** attribute

- The name of the attribute to be retrieved
**Returns:** The value of the attribute retrieved.
**Throws:** AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's getter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the getter.
**See Also:** setAttribute(javax.management.Attribute)

---

#### getAttribute

Object

getAttribute​(

String

attribute)
throws

AttributeNotFoundException

,

MBeanException

,

ReflectionException

Obtain the value of a specific attribute of the Dynamic MBean.

setAttribute

```java
void setAttribute​(
Attribute
attribute)
throws
AttributeNotFoundException
,

InvalidAttributeValueException
,

MBeanException
,

ReflectionException
```

Set the value of a specific attribute of the Dynamic MBean.

**Parameters:** attribute

- The identification of the attribute to
be set and the value it is to be set to.
**Throws:** AttributeNotFoundException

- if specified attribute does not exist or cannot be retrieved
**Throws:** InvalidAttributeValueException

- if value specified is not valid for the attribute
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's setter.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the MBean's setter.
**See Also:** getAttribute(java.lang.String)

---

#### setAttribute

void setAttribute​(

Attribute

attribute)
throws

AttributeNotFoundException

,

InvalidAttributeValueException

,

MBeanException

,

ReflectionException

Set the value of a specific attribute of the Dynamic MBean.

getAttributes

```java
AttributeList
getAttributes​(
String
[] attributes)
```

Get the values of several attributes of the Dynamic MBean.

**Parameters:** attributes

- A list of the attributes to be retrieved.
**Returns:** The list of attributes retrieved.
**See Also:** setAttributes(javax.management.AttributeList)

---

#### getAttributes

AttributeList

getAttributes​(

String

[] attributes)

Get the values of several attributes of the Dynamic MBean.

setAttributes

```java
AttributeList
setAttributes​(
AttributeList
attributes)
```

Sets the values of several attributes of the Dynamic MBean.

**Parameters:** attributes

- A list of attributes: The identification of the
attributes to be set and the values they are to be set to.
**Returns:** The list of attributes that were set, with their new values.
**See Also:** getAttributes(java.lang.String[])

---

#### setAttributes

AttributeList

setAttributes​(

AttributeList

attributes)

Sets the values of several attributes of the Dynamic MBean.

invoke

```java
Object
invoke​(
String
actionName,

Object
[] params,

String
[] signature)
throws
MBeanException
,

ReflectionException
```

Allows an action to be invoked on the Dynamic MBean.

**Parameters:** actionName

- The name of the action to be invoked.
**Parameters:** params

- An array containing the parameters to be set when the action is
invoked.
**Parameters:** signature

- An array containing the signature of the action. The class objects will
be loaded through the same class loader as the one used for loading the
MBean on which the action is invoked.
**Returns:** The object returned by the action, which represents the result of
invoking the action on the MBean specified.
**Throws:** MBeanException

- Wraps a

java.lang.Exception

thrown by the MBean's invoked method.
**Throws:** ReflectionException

- Wraps a

java.lang.Exception

thrown while trying to invoke the method

---

#### invoke

Object

invoke​(

String

actionName,

Object

[] params,

String

[] signature)
throws

MBeanException

,

ReflectionException

Allows an action to be invoked on the Dynamic MBean.

getMBeanInfo

```java
MBeanInfo
getMBeanInfo()
```

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

**Returns:** An instance of

MBeanInfo

allowing all attributes and actions
exposed by this Dynamic MBean to be retrieved.

---

#### getMBeanInfo

MBeanInfo

getMBeanInfo()

Provides the exposed attributes and actions of the Dynamic MBean using an MBeanInfo object.

---

