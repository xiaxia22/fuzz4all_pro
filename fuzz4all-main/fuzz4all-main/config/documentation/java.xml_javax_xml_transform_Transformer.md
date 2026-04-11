# Class Transformer

**Source:** `java.xml\javax\xml\transform\Transformer.html`

### Class Description

```java
public abstract class
Transformer

extends
Object
```

An instance of this abstract class can transform a
source tree into a result tree.

An instance of this class can be obtained with the

TransformerFactory.newTransformer

method. This instance may then be used to process XML from a
variety of sources and write the transformation output to a
variety of sinks.

An object of this class may not be used in multiple threads
running concurrently. Different Transformers may be used
concurrently by different threads.

A

Transformer

may be used multiple times. Parameters and
output properties are preserved across transformations.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Transformer()

Default constructor is protected on purpose.

---

### Method Details

#### public void reset()

Reset this

Transformer

to its original configuration.

Transformer

is reset to the same state as when it was created with

TransformerFactory.newTransformer()

,

TransformerFactory.newTransformer(Source source)

or

Templates.newTransformer()

.

reset()

is designed to allow the reuse of existing

Transformer

s
thus saving resources associated with the creation of new

Transformer

s.

The reset

Transformer

is not guaranteed to have the same

URIResolver

or

ErrorListener

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

URIResolver

and

ErrorListener

.

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method.

**Since:**
- 1.5

---

#### public abstract void transform​(
Source
xmlSource,

Result
outputTarget)
throws
TransformerException

Transform the XML

Source

to a

Result

.
Specific transformation behavior is determined by the settings of the

TransformerFactory

in effect when the

Transformer

was instantiated and any modifications made to
the

Transformer

instance.

An empty

Source

is represented as an empty document
as constructed by

DocumentBuilder.newDocument()

.
The result of transforming an empty

Source

depends on
the transformation behavior; it is not always an empty

Result

.

**Parameters:**
- xmlSource

- The XML input to transform.
- outputTarget

- The

Result

of transforming the

xmlSource

.

**Throws:**
- TransformerException

- If an unrecoverable error occurs
during the course of the transformation.

---

#### public abstract void setParameter​(
String
name,

Object
value)

Add a parameter for the transformation.

Pass a qualified name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

**Parameters:**
- name

- The name of the parameter, which may begin with a
namespace URI in curly braces ({}).
- value

- The value object. This can be any valid Java object. It is
up to the processor to provide the proper object coersion or to simply
pass the object on for use in an extension.

**Throws:**
- NullPointerException

- If value is null.

---

#### public abstract
Object
getParameter​(
String
name)

Get a parameter that was explicitly set with setParameter.

This method does not return a default parameter value, which
cannot be determined until the node context is evaluated during
the transformation process.

**Parameters:**
- name

- of

Object

to get

**Returns:**
- A parameter that has been set with setParameter.

---

#### public abstract void clearParameters()

Clear all parameters set with setParameter.

---

#### public abstract void setURIResolver​(
URIResolver
resolver)

Set an object that will be used to resolve URIs used in
document().

If the resolver argument is null, the URIResolver value will
be cleared and the transformer will no longer have a resolver.

**Parameters:**
- resolver

- An object that implements the URIResolver interface,
or null.

---

#### public abstract
URIResolver
getURIResolver()

Get an object that will be used to resolve URIs used in
document().

**Returns:**
- An object that implements the URIResolver interface,
or null.

---

#### public abstract void setOutputProperties​(
Properties
oformat)

Set the output properties for the transformation. These
properties will override properties set in the Templates
with xsl:output.

If argument to this function is null, any properties
previously set are removed, and the value will revert to the value
defined in the templates object.

Pass a qualified property key name as a two-part string, the namespace
URI enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

An

IllegalArgumentException

is thrown if any of the
argument keys are not recognized and are not namespace qualified.

**Parameters:**
- oformat

- A set of output properties that will be
used to override any of the same properties in affect
for the transformation.

**Throws:**
- IllegalArgumentException

- When keys are not recognized and
are not namespace qualified.

**See Also:**
- OutputKeys

,

Properties

---

#### public abstract
Properties
getOutputProperties()

Get a copy of the output properties for the transformation.

The properties returned should contain properties set by the user,
and properties set by the stylesheet, and these properties
are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the user or the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be the default Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, in the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, or in the stylesheet.

Note that mutation of the Properties object returned will not
effect the properties that the transformer contains.

If any of the argument keys are not recognized and are not
namespace qualified, the property will be ignored and not returned.
In other words the behaviour is not orthogonal with

setOutputProperties

.

**Returns:**
- A copy of the set of output properties in effect for
the next transformation.

**See Also:**
- OutputKeys

,

Properties

,

XSL Transformations (XSLT) Version 1.0

---

#### public abstract void setOutputProperty​(
String
name,

String
value)
throws
IllegalArgumentException

Set an output property that will be in effect for the
transformation.

Pass a qualified property name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

The Properties object that was passed to

setOutputProperties(java.util.Properties)

won't be effected by calling this method.

**Parameters:**
- name

- A non-null String that specifies an output
property name, which may be namespace qualified.
- value

- The non-null string value of the output property.

**Throws:**
- IllegalArgumentException

- If the property is not supported, and is
not qualified with a namespace.

**See Also:**
- OutputKeys

---

#### public abstract
String
getOutputProperty​(
String
name)
throws
IllegalArgumentException

Get an output property that is in effect for the transformer.

If a property has been set using

setOutputProperty(java.lang.String, java.lang.String)

,
that value will be returned. Otherwise, if a property is explicitly
specified in the stylesheet, that value will be returned. If
the value of the property has been defaulted, that is, if no
value has been set explicitly either with

setOutputProperty(java.lang.String, java.lang.String)

or
in the stylesheet, the result may vary depending on
implementation and input stylesheet.

**Parameters:**
- name

- A non-null String that specifies an output
property name, which may be namespace qualified.

**Returns:**
- The string value of the output property, or null
if no property was found.

**Throws:**
- IllegalArgumentException

- If the property is not supported.

**See Also:**
- OutputKeys

---

#### public abstract void setErrorListener​(
ErrorListener
listener)
throws
IllegalArgumentException

Set the error event listener in effect for the transformation.

**Parameters:**
- listener

- The new error listener.

**Throws:**
- IllegalArgumentException

- if listener is null.

---

#### public abstract
ErrorListener
getErrorListener()

Get the error event handler in effect for the transformation.
Implementations must provide a default error listener.

**Returns:**
- The current error handler, which should never be null.

---

### Additional Sections

#### Class Transformer

java.lang.Object

- javax.xml.transform.Transformer

javax.xml.transform.Transformer

```java
public abstract class
Transformer

extends
Object
```

An instance of this abstract class can transform a
source tree into a result tree.

An instance of this class can be obtained with the

TransformerFactory.newTransformer

method. This instance may then be used to process XML from a
variety of sources and write the transformation output to a
variety of sinks.

An object of this class may not be used in multiple threads
running concurrently. Different Transformers may be used
concurrently by different threads.

A

Transformer

may be used multiple times. Parameters and
output properties are preserved across transformations.

**Since:** 1.4

public abstract class

Transformer

extends

Object

An instance of this abstract class can transform a
source tree into a result tree.

An instance of this class can be obtained with the

TransformerFactory.newTransformer

method. This instance may then be used to process XML from a
variety of sources and write the transformation output to a
variety of sinks.

An object of this class may not be used in multiple threads
running concurrently. Different Transformers may be used
concurrently by different threads.

A

Transformer

may be used multiple times. Parameters and
output properties are preserved across transformations.

An instance of this class can be obtained with the

TransformerFactory.newTransformer

method. This instance may then be used to process XML from a
variety of sources and write the transformation output to a
variety of sinks.

An object of this class may not be used in multiple threads
running concurrently. Different Transformers may be used
concurrently by different threads.

A

Transformer

may be used multiple times. Parameters and
output properties are preserved across transformations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Transformer

()

Default constructor is protected on purpose.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

clearParameters

()

Clear all parameters set with setParameter.

abstract

ErrorListener

getErrorListener

()

Get the error event handler in effect for the transformation.

abstract

Properties

getOutputProperties

()

Get a copy of the output properties for the transformation.

abstract

String

getOutputProperty

​(

String

name)

Get an output property that is in effect for the transformer.

abstract

Object

getParameter

​(

String

name)

Get a parameter that was explicitly set with setParameter.

abstract

URIResolver

getURIResolver

()

Get an object that will be used to resolve URIs used in
document().

void

reset

()

Reset this

Transformer

to its original configuration.

abstract void

setErrorListener

​(

ErrorListener

listener)

Set the error event listener in effect for the transformation.

abstract void

setOutputProperties

​(

Properties

oformat)

Set the output properties for the transformation.

abstract void

setOutputProperty

​(

String

name,

String

value)

Set an output property that will be in effect for the
transformation.

abstract void

setParameter

​(

String

name,

Object

value)

Add a parameter for the transformation.

abstract void

setURIResolver

​(

URIResolver

resolver)

Set an object that will be used to resolve URIs used in
document().

abstract void

transform

​(

Source

xmlSource,

Result

outputTarget)

Transform the XML

Source

to a

Result

.

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

Modifier

Constructor

Description

protected

Transformer

()

Default constructor is protected on purpose.

---

#### Constructor Summary

Default constructor is protected on purpose.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

clearParameters

()

Clear all parameters set with setParameter.

abstract

ErrorListener

getErrorListener

()

Get the error event handler in effect for the transformation.

abstract

Properties

getOutputProperties

()

Get a copy of the output properties for the transformation.

abstract

String

getOutputProperty

​(

String

name)

Get an output property that is in effect for the transformer.

abstract

Object

getParameter

​(

String

name)

Get a parameter that was explicitly set with setParameter.

abstract

URIResolver

getURIResolver

()

Get an object that will be used to resolve URIs used in
document().

void

reset

()

Reset this

Transformer

to its original configuration.

abstract void

setErrorListener

​(

ErrorListener

listener)

Set the error event listener in effect for the transformation.

abstract void

setOutputProperties

​(

Properties

oformat)

Set the output properties for the transformation.

abstract void

setOutputProperty

​(

String

name,

String

value)

Set an output property that will be in effect for the
transformation.

abstract void

setParameter

​(

String

name,

Object

value)

Add a parameter for the transformation.

abstract void

setURIResolver

​(

URIResolver

resolver)

Set an object that will be used to resolve URIs used in
document().

abstract void

transform

​(

Source

xmlSource,

Result

outputTarget)

Transform the XML

Source

to a

Result

.

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

Clear all parameters set with setParameter.

Get the error event handler in effect for the transformation.

Get a copy of the output properties for the transformation.

Get an output property that is in effect for the transformer.

Get a parameter that was explicitly set with setParameter.

Get an object that will be used to resolve URIs used in
document().

Reset this

Transformer

to its original configuration.

Set the error event listener in effect for the transformation.

Set the output properties for the transformation.

Set an output property that will be in effect for the
transformation.

Add a parameter for the transformation.

Set an object that will be used to resolve URIs used in
document().

Transform the XML

Source

to a

Result

.

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

- Transformer

```java
protected Transformer()
```

Default constructor is protected on purpose.

============ METHOD DETAIL ==========

- Method Detail

- reset

```java
public void reset()
```

Reset this

Transformer

to its original configuration.

Transformer

is reset to the same state as when it was created with

TransformerFactory.newTransformer()

,

TransformerFactory.newTransformer(Source source)

or

Templates.newTransformer()

.

reset()

is designed to allow the reuse of existing

Transformer

s
thus saving resources associated with the creation of new

Transformer

s.

The reset

Transformer

is not guaranteed to have the same

URIResolver

or

ErrorListener

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

URIResolver

and

ErrorListener

.

**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- transform

```java
public abstract void transform​(
Source
xmlSource,

Result
outputTarget)
throws
TransformerException
```

Transform the XML

Source

to a

Result

.
Specific transformation behavior is determined by the settings of the

TransformerFactory

in effect when the

Transformer

was instantiated and any modifications made to
the

Transformer

instance.

An empty

Source

is represented as an empty document
as constructed by

DocumentBuilder.newDocument()

.
The result of transforming an empty

Source

depends on
the transformation behavior; it is not always an empty

Result

.

**Parameters:** xmlSource

- The XML input to transform.
**Parameters:** outputTarget

- The

Result

of transforming the

xmlSource

.
**Throws:** TransformerException

- If an unrecoverable error occurs
during the course of the transformation.

- setParameter

```java
public abstract void setParameter​(
String
name,

Object
value)
```

Add a parameter for the transformation.

Pass a qualified name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

**Parameters:** name

- The name of the parameter, which may begin with a
namespace URI in curly braces ({}).
**Parameters:** value

- The value object. This can be any valid Java object. It is
up to the processor to provide the proper object coersion or to simply
pass the object on for use in an extension.
**Throws:** NullPointerException

- If value is null.

- getParameter

```java
public abstract
Object
getParameter​(
String
name)
```

Get a parameter that was explicitly set with setParameter.

This method does not return a default parameter value, which
cannot be determined until the node context is evaluated during
the transformation process.

**Parameters:** name

- of

Object

to get
**Returns:** A parameter that has been set with setParameter.

- clearParameters

```java
public abstract void clearParameters()
```

Clear all parameters set with setParameter.

- setURIResolver

```java
public abstract void setURIResolver​(
URIResolver
resolver)
```

Set an object that will be used to resolve URIs used in
document().

If the resolver argument is null, the URIResolver value will
be cleared and the transformer will no longer have a resolver.

**Parameters:** resolver

- An object that implements the URIResolver interface,
or null.

- getURIResolver

```java
public abstract
URIResolver
getURIResolver()
```

Get an object that will be used to resolve URIs used in
document().

**Returns:** An object that implements the URIResolver interface,
or null.

- setOutputProperties

```java
public abstract void setOutputProperties​(
Properties
oformat)
```

Set the output properties for the transformation. These
properties will override properties set in the Templates
with xsl:output.

If argument to this function is null, any properties
previously set are removed, and the value will revert to the value
defined in the templates object.

Pass a qualified property key name as a two-part string, the namespace
URI enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

An

IllegalArgumentException

is thrown if any of the
argument keys are not recognized and are not namespace qualified.

**Parameters:** oformat

- A set of output properties that will be
used to override any of the same properties in affect
for the transformation.
**Throws:** IllegalArgumentException

- When keys are not recognized and
are not namespace qualified.
**See Also:** OutputKeys

,

Properties

- getOutputProperties

```java
public abstract
Properties
getOutputProperties()
```

Get a copy of the output properties for the transformation.

The properties returned should contain properties set by the user,
and properties set by the stylesheet, and these properties
are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the user or the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be the default Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, in the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, or in the stylesheet.

Note that mutation of the Properties object returned will not
effect the properties that the transformer contains.

If any of the argument keys are not recognized and are not
namespace qualified, the property will be ignored and not returned.
In other words the behaviour is not orthogonal with

setOutputProperties

.

**Returns:** A copy of the set of output properties in effect for
the next transformation.
**See Also:** OutputKeys

,

Properties

,

XSL Transformations (XSLT) Version 1.0

- setOutputProperty

```java
public abstract void setOutputProperty​(
String
name,

String
value)
throws
IllegalArgumentException
```

Set an output property that will be in effect for the
transformation.

Pass a qualified property name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

The Properties object that was passed to

setOutputProperties(java.util.Properties)

won't be effected by calling this method.

**Parameters:** name

- A non-null String that specifies an output
property name, which may be namespace qualified.
**Parameters:** value

- The non-null string value of the output property.
**Throws:** IllegalArgumentException

- If the property is not supported, and is
not qualified with a namespace.
**See Also:** OutputKeys

- getOutputProperty

```java
public abstract
String
getOutputProperty​(
String
name)
throws
IllegalArgumentException
```

Get an output property that is in effect for the transformer.

If a property has been set using

setOutputProperty(java.lang.String, java.lang.String)

,
that value will be returned. Otherwise, if a property is explicitly
specified in the stylesheet, that value will be returned. If
the value of the property has been defaulted, that is, if no
value has been set explicitly either with

setOutputProperty(java.lang.String, java.lang.String)

or
in the stylesheet, the result may vary depending on
implementation and input stylesheet.

**Parameters:** name

- A non-null String that specifies an output
property name, which may be namespace qualified.
**Returns:** The string value of the output property, or null
if no property was found.
**Throws:** IllegalArgumentException

- If the property is not supported.
**See Also:** OutputKeys

- setErrorListener

```java
public abstract void setErrorListener​(
ErrorListener
listener)
throws
IllegalArgumentException
```

Set the error event listener in effect for the transformation.

**Parameters:** listener

- The new error listener.
**Throws:** IllegalArgumentException

- if listener is null.

- getErrorListener

```java
public abstract
ErrorListener
getErrorListener()
```

Get the error event handler in effect for the transformation.
Implementations must provide a default error listener.

**Returns:** The current error handler, which should never be null.

Constructor Detail

- Transformer

```java
protected Transformer()
```

Default constructor is protected on purpose.

---

#### Constructor Detail

Transformer

```java
protected Transformer()
```

Default constructor is protected on purpose.

---

#### Transformer

protected Transformer()

Default constructor is protected on purpose.

Method Detail

- reset

```java
public void reset()
```

Reset this

Transformer

to its original configuration.

Transformer

is reset to the same state as when it was created with

TransformerFactory.newTransformer()

,

TransformerFactory.newTransformer(Source source)

or

Templates.newTransformer()

.

reset()

is designed to allow the reuse of existing

Transformer

s
thus saving resources associated with the creation of new

Transformer

s.

The reset

Transformer

is not guaranteed to have the same

URIResolver

or

ErrorListener

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

URIResolver

and

ErrorListener

.

**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- transform

```java
public abstract void transform​(
Source
xmlSource,

Result
outputTarget)
throws
TransformerException
```

Transform the XML

Source

to a

Result

.
Specific transformation behavior is determined by the settings of the

TransformerFactory

in effect when the

Transformer

was instantiated and any modifications made to
the

Transformer

instance.

An empty

Source

is represented as an empty document
as constructed by

DocumentBuilder.newDocument()

.
The result of transforming an empty

Source

depends on
the transformation behavior; it is not always an empty

Result

.

**Parameters:** xmlSource

- The XML input to transform.
**Parameters:** outputTarget

- The

Result

of transforming the

xmlSource

.
**Throws:** TransformerException

- If an unrecoverable error occurs
during the course of the transformation.

- setParameter

```java
public abstract void setParameter​(
String
name,

Object
value)
```

Add a parameter for the transformation.

Pass a qualified name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

**Parameters:** name

- The name of the parameter, which may begin with a
namespace URI in curly braces ({}).
**Parameters:** value

- The value object. This can be any valid Java object. It is
up to the processor to provide the proper object coersion or to simply
pass the object on for use in an extension.
**Throws:** NullPointerException

- If value is null.

- getParameter

```java
public abstract
Object
getParameter​(
String
name)
```

Get a parameter that was explicitly set with setParameter.

This method does not return a default parameter value, which
cannot be determined until the node context is evaluated during
the transformation process.

**Parameters:** name

- of

Object

to get
**Returns:** A parameter that has been set with setParameter.

- clearParameters

```java
public abstract void clearParameters()
```

Clear all parameters set with setParameter.

- setURIResolver

```java
public abstract void setURIResolver​(
URIResolver
resolver)
```

Set an object that will be used to resolve URIs used in
document().

If the resolver argument is null, the URIResolver value will
be cleared and the transformer will no longer have a resolver.

**Parameters:** resolver

- An object that implements the URIResolver interface,
or null.

- getURIResolver

```java
public abstract
URIResolver
getURIResolver()
```

Get an object that will be used to resolve URIs used in
document().

**Returns:** An object that implements the URIResolver interface,
or null.

- setOutputProperties

```java
public abstract void setOutputProperties​(
Properties
oformat)
```

Set the output properties for the transformation. These
properties will override properties set in the Templates
with xsl:output.

If argument to this function is null, any properties
previously set are removed, and the value will revert to the value
defined in the templates object.

Pass a qualified property key name as a two-part string, the namespace
URI enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

An

IllegalArgumentException

is thrown if any of the
argument keys are not recognized and are not namespace qualified.

**Parameters:** oformat

- A set of output properties that will be
used to override any of the same properties in affect
for the transformation.
**Throws:** IllegalArgumentException

- When keys are not recognized and
are not namespace qualified.
**See Also:** OutputKeys

,

Properties

- getOutputProperties

```java
public abstract
Properties
getOutputProperties()
```

Get a copy of the output properties for the transformation.

The properties returned should contain properties set by the user,
and properties set by the stylesheet, and these properties
are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the user or the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be the default Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, in the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, or in the stylesheet.

Note that mutation of the Properties object returned will not
effect the properties that the transformer contains.

If any of the argument keys are not recognized and are not
namespace qualified, the property will be ignored and not returned.
In other words the behaviour is not orthogonal with

setOutputProperties

.

**Returns:** A copy of the set of output properties in effect for
the next transformation.
**See Also:** OutputKeys

,

Properties

,

XSL Transformations (XSLT) Version 1.0

- setOutputProperty

```java
public abstract void setOutputProperty​(
String
name,

String
value)
throws
IllegalArgumentException
```

Set an output property that will be in effect for the
transformation.

Pass a qualified property name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

The Properties object that was passed to

setOutputProperties(java.util.Properties)

won't be effected by calling this method.

**Parameters:** name

- A non-null String that specifies an output
property name, which may be namespace qualified.
**Parameters:** value

- The non-null string value of the output property.
**Throws:** IllegalArgumentException

- If the property is not supported, and is
not qualified with a namespace.
**See Also:** OutputKeys

- getOutputProperty

```java
public abstract
String
getOutputProperty​(
String
name)
throws
IllegalArgumentException
```

Get an output property that is in effect for the transformer.

If a property has been set using

setOutputProperty(java.lang.String, java.lang.String)

,
that value will be returned. Otherwise, if a property is explicitly
specified in the stylesheet, that value will be returned. If
the value of the property has been defaulted, that is, if no
value has been set explicitly either with

setOutputProperty(java.lang.String, java.lang.String)

or
in the stylesheet, the result may vary depending on
implementation and input stylesheet.

**Parameters:** name

- A non-null String that specifies an output
property name, which may be namespace qualified.
**Returns:** The string value of the output property, or null
if no property was found.
**Throws:** IllegalArgumentException

- If the property is not supported.
**See Also:** OutputKeys

- setErrorListener

```java
public abstract void setErrorListener​(
ErrorListener
listener)
throws
IllegalArgumentException
```

Set the error event listener in effect for the transformation.

**Parameters:** listener

- The new error listener.
**Throws:** IllegalArgumentException

- if listener is null.

- getErrorListener

```java
public abstract
ErrorListener
getErrorListener()
```

Get the error event handler in effect for the transformation.
Implementations must provide a default error listener.

**Returns:** The current error handler, which should never be null.

---

#### Method Detail

reset

```java
public void reset()
```

Reset this

Transformer

to its original configuration.

Transformer

is reset to the same state as when it was created with

TransformerFactory.newTransformer()

,

TransformerFactory.newTransformer(Source source)

or

Templates.newTransformer()

.

reset()

is designed to allow the reuse of existing

Transformer

s
thus saving resources associated with the creation of new

Transformer

s.

The reset

Transformer

is not guaranteed to have the same

URIResolver

or

ErrorListener

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

URIResolver

and

ErrorListener

.

**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

---

#### reset

public void reset()

Reset this

Transformer

to its original configuration.

Transformer

is reset to the same state as when it was created with

TransformerFactory.newTransformer()

,

TransformerFactory.newTransformer(Source source)

or

Templates.newTransformer()

.

reset()

is designed to allow the reuse of existing

Transformer

s
thus saving resources associated with the creation of new

Transformer

s.

The reset

Transformer

is not guaranteed to have the same

URIResolver

or

ErrorListener

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

URIResolver

and

ErrorListener

.

Reset this

Transformer

to its original configuration.

Transformer

is reset to the same state as when it was created with

TransformerFactory.newTransformer()

,

TransformerFactory.newTransformer(Source source)

or

Templates.newTransformer()

.

reset()

is designed to allow the reuse of existing

Transformer

s
thus saving resources associated with the creation of new

Transformer

s.

The reset

Transformer

is not guaranteed to have the same

URIResolver

or

ErrorListener

Object

s, e.g.

Object.equals(Object obj)

.
It is guaranteed to have a functionally equal

URIResolver

and

ErrorListener

.

transform

```java
public abstract void transform​(
Source
xmlSource,

Result
outputTarget)
throws
TransformerException
```

Transform the XML

Source

to a

Result

.
Specific transformation behavior is determined by the settings of the

TransformerFactory

in effect when the

Transformer

was instantiated and any modifications made to
the

Transformer

instance.

An empty

Source

is represented as an empty document
as constructed by

DocumentBuilder.newDocument()

.
The result of transforming an empty

Source

depends on
the transformation behavior; it is not always an empty

Result

.

**Parameters:** xmlSource

- The XML input to transform.
**Parameters:** outputTarget

- The

Result

of transforming the

xmlSource

.
**Throws:** TransformerException

- If an unrecoverable error occurs
during the course of the transformation.

---

#### transform

public abstract void transform​(

Source

xmlSource,

Result

outputTarget)
throws

TransformerException

Transform the XML

Source

to a

Result

.
Specific transformation behavior is determined by the settings of the

TransformerFactory

in effect when the

Transformer

was instantiated and any modifications made to
the

Transformer

instance.

An empty

Source

is represented as an empty document
as constructed by

DocumentBuilder.newDocument()

.
The result of transforming an empty

Source

depends on
the transformation behavior; it is not always an empty

Result

.

Transform the XML

Source

to a

Result

.
Specific transformation behavior is determined by the settings of the

TransformerFactory

in effect when the

Transformer

was instantiated and any modifications made to
the

Transformer

instance.

An empty

Source

is represented as an empty document
as constructed by

DocumentBuilder.newDocument()

.
The result of transforming an empty

Source

depends on
the transformation behavior; it is not always an empty

Result

.

setParameter

```java
public abstract void setParameter​(
String
name,

Object
value)
```

Add a parameter for the transformation.

Pass a qualified name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

**Parameters:** name

- The name of the parameter, which may begin with a
namespace URI in curly braces ({}).
**Parameters:** value

- The value object. This can be any valid Java object. It is
up to the processor to provide the proper object coersion or to simply
pass the object on for use in an extension.
**Throws:** NullPointerException

- If value is null.

---

#### setParameter

public abstract void setParameter​(

String

name,

Object

value)

Add a parameter for the transformation.

Pass a qualified name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

Pass a qualified name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

getParameter

```java
public abstract
Object
getParameter​(
String
name)
```

Get a parameter that was explicitly set with setParameter.

This method does not return a default parameter value, which
cannot be determined until the node context is evaluated during
the transformation process.

**Parameters:** name

- of

Object

to get
**Returns:** A parameter that has been set with setParameter.

---

#### getParameter

public abstract

Object

getParameter​(

String

name)

Get a parameter that was explicitly set with setParameter.

This method does not return a default parameter value, which
cannot be determined until the node context is evaluated during
the transformation process.

This method does not return a default parameter value, which
cannot be determined until the node context is evaluated during
the transformation process.

clearParameters

```java
public abstract void clearParameters()
```

Clear all parameters set with setParameter.

---

#### clearParameters

public abstract void clearParameters()

Clear all parameters set with setParameter.

setURIResolver

```java
public abstract void setURIResolver​(
URIResolver
resolver)
```

Set an object that will be used to resolve URIs used in
document().

If the resolver argument is null, the URIResolver value will
be cleared and the transformer will no longer have a resolver.

**Parameters:** resolver

- An object that implements the URIResolver interface,
or null.

---

#### setURIResolver

public abstract void setURIResolver​(

URIResolver

resolver)

Set an object that will be used to resolve URIs used in
document().

If the resolver argument is null, the URIResolver value will
be cleared and the transformer will no longer have a resolver.

If the resolver argument is null, the URIResolver value will
be cleared and the transformer will no longer have a resolver.

getURIResolver

```java
public abstract
URIResolver
getURIResolver()
```

Get an object that will be used to resolve URIs used in
document().

**Returns:** An object that implements the URIResolver interface,
or null.

---

#### getURIResolver

public abstract

URIResolver

getURIResolver()

Get an object that will be used to resolve URIs used in
document().

setOutputProperties

```java
public abstract void setOutputProperties​(
Properties
oformat)
```

Set the output properties for the transformation. These
properties will override properties set in the Templates
with xsl:output.

If argument to this function is null, any properties
previously set are removed, and the value will revert to the value
defined in the templates object.

Pass a qualified property key name as a two-part string, the namespace
URI enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

An

IllegalArgumentException

is thrown if any of the
argument keys are not recognized and are not namespace qualified.

**Parameters:** oformat

- A set of output properties that will be
used to override any of the same properties in affect
for the transformation.
**Throws:** IllegalArgumentException

- When keys are not recognized and
are not namespace qualified.
**See Also:** OutputKeys

,

Properties

---

#### setOutputProperties

public abstract void setOutputProperties​(

Properties

oformat)

Set the output properties for the transformation. These
properties will override properties set in the Templates
with xsl:output.

If argument to this function is null, any properties
previously set are removed, and the value will revert to the value
defined in the templates object.

Pass a qualified property key name as a two-part string, the namespace
URI enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

An

IllegalArgumentException

is thrown if any of the
argument keys are not recognized and are not namespace qualified.

If argument to this function is null, any properties
previously set are removed, and the value will revert to the value
defined in the templates object.

Pass a qualified property key name as a two-part string, the namespace
URI enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

getOutputProperties

```java
public abstract
Properties
getOutputProperties()
```

Get a copy of the output properties for the transformation.

The properties returned should contain properties set by the user,
and properties set by the stylesheet, and these properties
are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the user or the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be the default Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, in the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, or in the stylesheet.

Note that mutation of the Properties object returned will not
effect the properties that the transformer contains.

If any of the argument keys are not recognized and are not
namespace qualified, the property will be ignored and not returned.
In other words the behaviour is not orthogonal with

setOutputProperties

.

**Returns:** A copy of the set of output properties in effect for
the next transformation.
**See Also:** OutputKeys

,

Properties

,

XSL Transformations (XSLT) Version 1.0

---

#### getOutputProperties

public abstract

Properties

getOutputProperties()

Get a copy of the output properties for the transformation.

The properties returned should contain properties set by the user,
and properties set by the stylesheet, and these properties
are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the user or the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be the default Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, in the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, or in the stylesheet.

Note that mutation of the Properties object returned will not
effect the properties that the transformer contains.

If any of the argument keys are not recognized and are not
namespace qualified, the property will be ignored and not returned.
In other words the behaviour is not orthogonal with

setOutputProperties

.

Get a copy of the output properties for the transformation.

The properties returned should contain properties set by the user,
and properties set by the stylesheet, and these properties
are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the user or the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be the default Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, in the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set by

setOutputProperty(java.lang.String, java.lang.String)

,

setOutputProperties(java.util.Properties)

, or in the stylesheet.

Note that mutation of the Properties object returned will not
effect the properties that the transformer contains.

If any of the argument keys are not recognized and are not
namespace qualified, the property will be ignored and not returned.
In other words the behaviour is not orthogonal with

setOutputProperties

.

setOutputProperty

```java
public abstract void setOutputProperty​(
String
name,

String
value)
throws
IllegalArgumentException
```

Set an output property that will be in effect for the
transformation.

Pass a qualified property name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

The Properties object that was passed to

setOutputProperties(java.util.Properties)

won't be effected by calling this method.

**Parameters:** name

- A non-null String that specifies an output
property name, which may be namespace qualified.
**Parameters:** value

- The non-null string value of the output property.
**Throws:** IllegalArgumentException

- If the property is not supported, and is
not qualified with a namespace.
**See Also:** OutputKeys

---

#### setOutputProperty

public abstract void setOutputProperty​(

String

name,

String

value)
throws

IllegalArgumentException

Set an output property that will be in effect for the
transformation.

Pass a qualified property name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

The Properties object that was passed to

setOutputProperties(java.util.Properties)

won't be effected by calling this method.

Pass a qualified property name as a two-part string, the namespace URI
enclosed in curly braces ({}), followed by the local name. If the
name has a null URL, the String only contain the local name. An
application can safely check for a non-null URI by testing to see if the
first character of the name is a '{' character.

For example, if a URI and local name were obtained from an element
defined with <xyz:foo
xmlns:xyz="http://xyz.foo.com/yada/baz.html"/>,
then the qualified name would be "{http://xyz.foo.com/yada/baz.html}foo".
Note that no prefix is used.

The Properties object that was passed to

setOutputProperties(java.util.Properties)

won't be effected by calling this method.

getOutputProperty

```java
public abstract
String
getOutputProperty​(
String
name)
throws
IllegalArgumentException
```

Get an output property that is in effect for the transformer.

If a property has been set using

setOutputProperty(java.lang.String, java.lang.String)

,
that value will be returned. Otherwise, if a property is explicitly
specified in the stylesheet, that value will be returned. If
the value of the property has been defaulted, that is, if no
value has been set explicitly either with

setOutputProperty(java.lang.String, java.lang.String)

or
in the stylesheet, the result may vary depending on
implementation and input stylesheet.

**Parameters:** name

- A non-null String that specifies an output
property name, which may be namespace qualified.
**Returns:** The string value of the output property, or null
if no property was found.
**Throws:** IllegalArgumentException

- If the property is not supported.
**See Also:** OutputKeys

---

#### getOutputProperty

public abstract

String

getOutputProperty​(

String

name)
throws

IllegalArgumentException

Get an output property that is in effect for the transformer.

If a property has been set using

setOutputProperty(java.lang.String, java.lang.String)

,
that value will be returned. Otherwise, if a property is explicitly
specified in the stylesheet, that value will be returned. If
the value of the property has been defaulted, that is, if no
value has been set explicitly either with

setOutputProperty(java.lang.String, java.lang.String)

or
in the stylesheet, the result may vary depending on
implementation and input stylesheet.

Get an output property that is in effect for the transformer.

If a property has been set using

setOutputProperty(java.lang.String, java.lang.String)

,
that value will be returned. Otherwise, if a property is explicitly
specified in the stylesheet, that value will be returned. If
the value of the property has been defaulted, that is, if no
value has been set explicitly either with

setOutputProperty(java.lang.String, java.lang.String)

or
in the stylesheet, the result may vary depending on
implementation and input stylesheet.

setErrorListener

```java
public abstract void setErrorListener​(
ErrorListener
listener)
throws
IllegalArgumentException
```

Set the error event listener in effect for the transformation.

**Parameters:** listener

- The new error listener.
**Throws:** IllegalArgumentException

- if listener is null.

---

#### setErrorListener

public abstract void setErrorListener​(

ErrorListener

listener)
throws

IllegalArgumentException

Set the error event listener in effect for the transformation.

getErrorListener

```java
public abstract
ErrorListener
getErrorListener()
```

Get the error event handler in effect for the transformation.
Implementations must provide a default error listener.

**Returns:** The current error handler, which should never be null.

---

#### getErrorListener

public abstract

ErrorListener

getErrorListener()

Get the error event handler in effect for the transformation.
Implementations must provide a default error listener.

---

