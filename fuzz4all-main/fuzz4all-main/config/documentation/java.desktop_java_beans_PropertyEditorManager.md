# Class PropertyEditorManager

**Source:** `java.desktop\java\beans\PropertyEditorManager.html`

### Class Description

```java
public class
PropertyEditorManager

extends
Object
```

The PropertyEditorManager can be used to locate a property editor for
any given type name. This property editor must support the
java.beans.PropertyEditor interface for editing a given object.

The PropertyEditorManager uses three techniques for locating an editor
for a given type. First, it provides a registerEditor method to allow
an editor to be specifically registered for a given type. Second it
tries to locate a suitable class by adding "Editor" to the full
qualified classname of the given type (e.g. "foo.bah.FozEditor").
Finally it takes the simple classname (without the package name) adds
"Editor" to it and looks in a search-path of packages for a matching
class.

So for an input class foo.bah.Fred, the PropertyEditorManager would
first look in its tables to see if an editor had been registered for
foo.bah.Fred and if so use that. Then it will look for a
foo.bah.FredEditor class. Then it will look for (say)
standardEditorsPackage.FredEditor class.

Default PropertyEditors will be provided for the Java primitive types
"boolean", "byte", "short", "int", "long", "float", and "double"; and
for the classes java.lang.String. java.awt.Color, and java.awt.Font.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

#### public PropertyEditorManager()

*No description found.*

---

### Method Details

#### public static void registerEditor​(
Class
<?> targetType,

Class
<?> editorClass)

Registers an editor class to edit values of the given target class.
If the editor class is

null

,
then any existing definition will be removed.
Thus this method can be used to cancel the registration.
The registration is canceled automatically
if either the target or editor class is unloaded.

If there is a security manager, its

checkPropertiesAccess

method is called. This could result in a

SecurityException

.

**Parameters:**
- targetType

- the class object of the type to be edited
- editorClass

- the class object of the editor class

**Throws:**
- SecurityException

- if a security manager exists and
its

checkPropertiesAccess

method
doesn't allow setting of system properties

**See Also:**
- SecurityManager.checkPropertiesAccess()

---

#### public static
PropertyEditor
findEditor​(
Class
<?> targetType)

Locate a value editor for a given target type.

**Parameters:**
- targetType

- The Class object for the type to be edited

**Returns:**
- An editor object for the given target class.
The result is null if no suitable editor can be found.

---

#### public static
String
[] getEditorSearchPath()

Gets the package names that will be searched for property editors.

**Returns:**
- The array of package names that will be searched in
order to find property editors.

The default value for this array is implementation-dependent,
e.g. Sun implementation initially sets to {"sun.beans.editors"}.

---

#### public static void setEditorSearchPath​(
String
[] path)

Change the list of package names that will be used for
finding property editors.

First, if there is a security manager, its

checkPropertiesAccess

method is called. This could result in a SecurityException.

**Parameters:**
- path

- Array of package names.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow setting
of system properties.

**See Also:**
- SecurityManager.checkPropertiesAccess()

---

### Additional Sections

#### Class PropertyEditorManager

java.lang.Object

- java.beans.PropertyEditorManager

java.beans.PropertyEditorManager

```java
public class
PropertyEditorManager

extends
Object
```

The PropertyEditorManager can be used to locate a property editor for
any given type name. This property editor must support the
java.beans.PropertyEditor interface for editing a given object.

The PropertyEditorManager uses three techniques for locating an editor
for a given type. First, it provides a registerEditor method to allow
an editor to be specifically registered for a given type. Second it
tries to locate a suitable class by adding "Editor" to the full
qualified classname of the given type (e.g. "foo.bah.FozEditor").
Finally it takes the simple classname (without the package name) adds
"Editor" to it and looks in a search-path of packages for a matching
class.

So for an input class foo.bah.Fred, the PropertyEditorManager would
first look in its tables to see if an editor had been registered for
foo.bah.Fred and if so use that. Then it will look for a
foo.bah.FredEditor class. Then it will look for (say)
standardEditorsPackage.FredEditor class.

Default PropertyEditors will be provided for the Java primitive types
"boolean", "byte", "short", "int", "long", "float", and "double"; and
for the classes java.lang.String. java.awt.Color, and java.awt.Font.

**Since:** 1.1

public class

PropertyEditorManager

extends

Object

The PropertyEditorManager can be used to locate a property editor for
any given type name. This property editor must support the
java.beans.PropertyEditor interface for editing a given object.

The PropertyEditorManager uses three techniques for locating an editor
for a given type. First, it provides a registerEditor method to allow
an editor to be specifically registered for a given type. Second it
tries to locate a suitable class by adding "Editor" to the full
qualified classname of the given type (e.g. "foo.bah.FozEditor").
Finally it takes the simple classname (without the package name) adds
"Editor" to it and looks in a search-path of packages for a matching
class.

So for an input class foo.bah.Fred, the PropertyEditorManager would
first look in its tables to see if an editor had been registered for
foo.bah.Fred and if so use that. Then it will look for a
foo.bah.FredEditor class. Then it will look for (say)
standardEditorsPackage.FredEditor class.

Default PropertyEditors will be provided for the Java primitive types
"boolean", "byte", "short", "int", "long", "float", and "double"; and
for the classes java.lang.String. java.awt.Color, and java.awt.Font.

The PropertyEditorManager uses three techniques for locating an editor
for a given type. First, it provides a registerEditor method to allow
an editor to be specifically registered for a given type. Second it
tries to locate a suitable class by adding "Editor" to the full
qualified classname of the given type (e.g. "foo.bah.FozEditor").
Finally it takes the simple classname (without the package name) adds
"Editor" to it and looks in a search-path of packages for a matching
class.

So for an input class foo.bah.Fred, the PropertyEditorManager would
first look in its tables to see if an editor had been registered for
foo.bah.Fred and if so use that. Then it will look for a
foo.bah.FredEditor class. Then it will look for (say)
standardEditorsPackage.FredEditor class.

Default PropertyEditors will be provided for the Java primitive types
"boolean", "byte", "short", "int", "long", "float", and "double"; and
for the classes java.lang.String. java.awt.Color, and java.awt.Font.

So for an input class foo.bah.Fred, the PropertyEditorManager would
first look in its tables to see if an editor had been registered for
foo.bah.Fred and if so use that. Then it will look for a
foo.bah.FredEditor class. Then it will look for (say)
standardEditorsPackage.FredEditor class.

Default PropertyEditors will be provided for the Java primitive types
"boolean", "byte", "short", "int", "long", "float", and "double"; and
for the classes java.lang.String. java.awt.Color, and java.awt.Font.

Default PropertyEditors will be provided for the Java primitive types
"boolean", "byte", "short", "int", "long", "float", and "double"; and
for the classes java.lang.String. java.awt.Color, and java.awt.Font.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PropertyEditorManager

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PropertyEditor

findEditor

​(

Class

<?> targetType)

Locate a value editor for a given target type.

static

String

[]

getEditorSearchPath

()

Gets the package names that will be searched for property editors.

static void

registerEditor

​(

Class

<?> targetType,

Class

<?> editorClass)

Registers an editor class to edit values of the given target class.

static void

setEditorSearchPath

​(

String

[] path)

Change the list of package names that will be used for
finding property editors.

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

PropertyEditorManager

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

PropertyEditor

findEditor

​(

Class

<?> targetType)

Locate a value editor for a given target type.

static

String

[]

getEditorSearchPath

()

Gets the package names that will be searched for property editors.

static void

registerEditor

​(

Class

<?> targetType,

Class

<?> editorClass)

Registers an editor class to edit values of the given target class.

static void

setEditorSearchPath

​(

String

[] path)

Change the list of package names that will be used for
finding property editors.

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

Locate a value editor for a given target type.

Gets the package names that will be searched for property editors.

Registers an editor class to edit values of the given target class.

Change the list of package names that will be used for
finding property editors.

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

- PropertyEditorManager

```java
public PropertyEditorManager()
```

============ METHOD DETAIL ==========

- Method Detail

- registerEditor

```java
public static void registerEditor​(
Class
<?> targetType,

Class
<?> editorClass)
```

Registers an editor class to edit values of the given target class.
If the editor class is

null

,
then any existing definition will be removed.
Thus this method can be used to cancel the registration.
The registration is canceled automatically
if either the target or editor class is unloaded.

If there is a security manager, its

checkPropertiesAccess

method is called. This could result in a

SecurityException

.

**Parameters:** targetType

- the class object of the type to be edited
**Parameters:** editorClass

- the class object of the editor class
**Throws:** SecurityException

- if a security manager exists and
its

checkPropertiesAccess

method
doesn't allow setting of system properties
**See Also:** SecurityManager.checkPropertiesAccess()

- findEditor

```java
public static
PropertyEditor
findEditor​(
Class
<?> targetType)
```

Locate a value editor for a given target type.

**Parameters:** targetType

- The Class object for the type to be edited
**Returns:** An editor object for the given target class.
The result is null if no suitable editor can be found.

- getEditorSearchPath

```java
public static
String
[] getEditorSearchPath()
```

Gets the package names that will be searched for property editors.

**Returns:** The array of package names that will be searched in
order to find property editors.

The default value for this array is implementation-dependent,
e.g. Sun implementation initially sets to {"sun.beans.editors"}.

- setEditorSearchPath

```java
public static void setEditorSearchPath​(
String
[] path)
```

Change the list of package names that will be used for
finding property editors.

First, if there is a security manager, its

checkPropertiesAccess

method is called. This could result in a SecurityException.

**Parameters:** path

- Array of package names.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow setting
of system properties.
**See Also:** SecurityManager.checkPropertiesAccess()

Constructor Detail

- PropertyEditorManager

```java
public PropertyEditorManager()
```

---

#### Constructor Detail

PropertyEditorManager

```java
public PropertyEditorManager()
```

---

#### PropertyEditorManager

public PropertyEditorManager()

Method Detail

- registerEditor

```java
public static void registerEditor​(
Class
<?> targetType,

Class
<?> editorClass)
```

Registers an editor class to edit values of the given target class.
If the editor class is

null

,
then any existing definition will be removed.
Thus this method can be used to cancel the registration.
The registration is canceled automatically
if either the target or editor class is unloaded.

If there is a security manager, its

checkPropertiesAccess

method is called. This could result in a

SecurityException

.

**Parameters:** targetType

- the class object of the type to be edited
**Parameters:** editorClass

- the class object of the editor class
**Throws:** SecurityException

- if a security manager exists and
its

checkPropertiesAccess

method
doesn't allow setting of system properties
**See Also:** SecurityManager.checkPropertiesAccess()

- findEditor

```java
public static
PropertyEditor
findEditor​(
Class
<?> targetType)
```

Locate a value editor for a given target type.

**Parameters:** targetType

- The Class object for the type to be edited
**Returns:** An editor object for the given target class.
The result is null if no suitable editor can be found.

- getEditorSearchPath

```java
public static
String
[] getEditorSearchPath()
```

Gets the package names that will be searched for property editors.

**Returns:** The array of package names that will be searched in
order to find property editors.

The default value for this array is implementation-dependent,
e.g. Sun implementation initially sets to {"sun.beans.editors"}.

- setEditorSearchPath

```java
public static void setEditorSearchPath​(
String
[] path)
```

Change the list of package names that will be used for
finding property editors.

First, if there is a security manager, its

checkPropertiesAccess

method is called. This could result in a SecurityException.

**Parameters:** path

- Array of package names.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow setting
of system properties.
**See Also:** SecurityManager.checkPropertiesAccess()

---

#### Method Detail

registerEditor

```java
public static void registerEditor​(
Class
<?> targetType,

Class
<?> editorClass)
```

Registers an editor class to edit values of the given target class.
If the editor class is

null

,
then any existing definition will be removed.
Thus this method can be used to cancel the registration.
The registration is canceled automatically
if either the target or editor class is unloaded.

If there is a security manager, its

checkPropertiesAccess

method is called. This could result in a

SecurityException

.

**Parameters:** targetType

- the class object of the type to be edited
**Parameters:** editorClass

- the class object of the editor class
**Throws:** SecurityException

- if a security manager exists and
its

checkPropertiesAccess

method
doesn't allow setting of system properties
**See Also:** SecurityManager.checkPropertiesAccess()

---

#### registerEditor

public static void registerEditor​(

Class

<?> targetType,

Class

<?> editorClass)

Registers an editor class to edit values of the given target class.
If the editor class is

null

,
then any existing definition will be removed.
Thus this method can be used to cancel the registration.
The registration is canceled automatically
if either the target or editor class is unloaded.

If there is a security manager, its

checkPropertiesAccess

method is called. This could result in a

SecurityException

.

If there is a security manager, its

checkPropertiesAccess

method is called. This could result in a

SecurityException

.

findEditor

```java
public static
PropertyEditor
findEditor​(
Class
<?> targetType)
```

Locate a value editor for a given target type.

**Parameters:** targetType

- The Class object for the type to be edited
**Returns:** An editor object for the given target class.
The result is null if no suitable editor can be found.

---

#### findEditor

public static

PropertyEditor

findEditor​(

Class

<?> targetType)

Locate a value editor for a given target type.

getEditorSearchPath

```java
public static
String
[] getEditorSearchPath()
```

Gets the package names that will be searched for property editors.

**Returns:** The array of package names that will be searched in
order to find property editors.

The default value for this array is implementation-dependent,
e.g. Sun implementation initially sets to {"sun.beans.editors"}.

---

#### getEditorSearchPath

public static

String

[] getEditorSearchPath()

Gets the package names that will be searched for property editors.

The default value for this array is implementation-dependent,
e.g. Sun implementation initially sets to {"sun.beans.editors"}.

setEditorSearchPath

```java
public static void setEditorSearchPath​(
String
[] path)
```

Change the list of package names that will be used for
finding property editors.

First, if there is a security manager, its

checkPropertiesAccess

method is called. This could result in a SecurityException.

**Parameters:** path

- Array of package names.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow setting
of system properties.
**See Also:** SecurityManager.checkPropertiesAccess()

---

#### setEditorSearchPath

public static void setEditorSearchPath​(

String

[] path)

Change the list of package names that will be used for
finding property editors.

First, if there is a security manager, its

checkPropertiesAccess

method is called. This could result in a SecurityException.

First, if there is a security manager, its

checkPropertiesAccess

method is called. This could result in a SecurityException.

---

