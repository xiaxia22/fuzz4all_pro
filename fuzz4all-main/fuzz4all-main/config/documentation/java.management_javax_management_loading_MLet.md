# Class MLet

**Source:** `java.management\javax\management\loading\MLet.html`

### Class Description

```java
public class
MLet

extends
URLClassLoader

implements
MLetMBean
,
MBeanRegistration
,
Externalizable
```

Allows you to instantiate and register one or several MBeans in the MBean server
coming from a remote URL. M-let is a shortcut for management applet. The m-let service does this
by loading an m-let text file, which specifies information on the MBeans to be obtained.
The information on each MBean is specified in a single instance of a tag, called the MLET tag.
The location of the m-let text file is specified by a URL.

The

MLET

tag has the following syntax:

<

MLET

CODE =

class

| OBJECT =

serfile

ARCHIVE = "

archiveList

"

[CODEBASE =

codebaseURL

]

[NAME =

mbeanname

]

[VERSION =

version

]

>

[

arglist

]

<

/MLET

>

where:

**CODE = class:** This attribute specifies the full Java class name, including package name, of the MBean to be obtained.
The compiled

.class

file of the MBean must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. Either

CODE

or

OBJECT

must be present.
**OBJECT = serfile:** This attribute specifies the

.ser

file that contains a serialized representation of the MBean to be obtained.
This file must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. If the

.jar

file contains a directory hierarchy, specify the path of the file within this hierarchy. Otherwise a match will not be found. Either

CODE

or

OBJECT

must be present.
**ARCHIVE = " archiveList ":** This mandatory attribute specifies one or more

.jar

files
containing MBeans or other resources used by
the MBean to be obtained. One of the

.jar

files must contain the file specified by the

CODE

or

OBJECT

attribute.
If archivelist contains more than one file:

- Each file must be separated from the one that follows it by a comma (,).

archivelist

must be enclosed in double quote marks.

All

.jar

files in

archivelist

must be stored in the directory specified by the code base URL.
**CODEBASE = codebaseURL:** This optional attribute specifies the code base URL of the MBean to be obtained. It identifies the directory that contains
the

.jar

files specified by the

ARCHIVE

attribute. Specify this attribute only if the

.jar

files are not in the same
directory as the m-let text file. If this attribute is not specified, the base URL of the m-let text file is used.
**NAME = mbeanname:** This optional attribute specifies the object name to be assigned to the
MBean instance when the m-let service registers it. If

mbeanname

starts with the colon character (:), the domain
part of the object name is the default domain of the MBean server,
as returned by

MBeanServerConnection.getDefaultDomain()

.
**VERSION = version:** This optional attribute specifies the version number of the MBean and
associated

.jar

files to be obtained. This version number can
be used to specify that the

.jar

files are loaded from the
server to update those stored locally in the cache the next time the m-let
text file is loaded.

version

must be a series of non-negative
decimal integers each separated by a period from the one that precedes it.
**arglist:** This optional attribute specifies a list of one or more parameters for the
MBean to be instantiated. This list describes the parameters to be passed the MBean's constructor.
Use the following syntax to specify each item in

arglist

:

**< ARG TYPE= argumentType VALUE= value >:** where:

- argumentType

is the type of the argument that will be passed as parameter to the MBean's constructor.

The arguments' type in the argument list should be a Java primitive type or a Java basic type
(

java.lang.Boolean, java.lang.Byte, java.lang.Short, java.lang.Long, java.lang.Integer, java.lang.Float, java.lang.Double, java.lang.String

).

When an m-let text file is loaded, an
instance of each MBean specified in the file is created and registered.

The m-let service extends the

java.net.URLClassLoader

and can be used to load remote classes
and jar files in the VM of the agent.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

**All Implemented Interfaces:** Closeable

,

Externalizable

,

Serializable

,

AutoCloseable

,

MLetMBean

,

MBeanRegistration

---

### Field Details

*No entries found.*

### Constructor Details

#### public MLet()

Constructs a new MLet using the default delegation parent ClassLoader.

---

#### public MLet​(
URL
[] urls)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:**
- urls

- The URLs from which to load classes and resources.

---

#### public MLet​(
URL
[] urls,

ClassLoader
parent)

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- parent

- The parent class loader for delegation.

---

#### public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- parent

- The parent class loader for delegation.
- factory

- The URLStreamHandlerFactory to use when creating URLs.

---

#### public MLet​(
URL
[] urls,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### public MLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- parent

- The parent class loader for delegation.
- delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:**
- urls

- The URLs from which to load classes and resources.
- parent

- The parent class loader for delegation.
- factory

- The URLStreamHandlerFactory to use when creating URLs.
- delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

### Method Details

#### public void addURL​(
URL
url)

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:**
- addURL

in interface

MLetMBean

**Overrides:**
- addURL

in class

URLClassLoader

**Parameters:**
- url

- the URL to be added to the search path of URLs

---

#### public void addURL​(
String
url)
throws
ServiceNotFoundException

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:**
- addURL

in interface

MLetMBean

**Parameters:**
- url

- the URL to add.

**Throws:**
- ServiceNotFoundException

- The specified URL is malformed.

---

#### public
URL
[] getURLs()

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Specified by:**
- getURLs

in interface

MLetMBean

**Overrides:**
- getURLs

in class

URLClassLoader

**Returns:**
- the search path of URLs for loading classes and resources.

---

#### public
Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:**
- getMBeansFromURL

in interface

MLetMBean

**Parameters:**
- url

- The URL of the text file to be loaded as URL object.

**Returns:**
- A set containing one entry per MLET tag in the m-let text file loaded.
Each entry specifies either the ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be created.

**Throws:**
- ServiceNotFoundException

- One of the following errors has occurred: The m-let text file does
not contain an MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the value of url is
null.
- IllegalStateException

- MLet MBean is not registered with an MBeanServer.

---

#### public
Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:**
- getMBeansFromURL

in interface

MLetMBean

**Parameters:**
- url

- The URL of the text file to be loaded as String object.

**Returns:**
- A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.

**Throws:**
- ServiceNotFoundException

- One of the following
errors has occurred: The m-let text file does not contain an
MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the url is
malformed.
- IllegalStateException

- MLet MBean is not registered
with an MBeanServer.

---

#### public
String
getLibraryDirectory()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Specified by:**
- getLibraryDirectory

in interface

MLetMBean

**Returns:**
- The current directory used by the library loader.

**Throws:**
- UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.

**See Also:**
- setLibraryDirectory(java.lang.String)

---

#### public void setLibraryDirectory​(
String
libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Specified by:**
- setLibraryDirectory

in interface

MLetMBean

**Parameters:**
- libdir

- The directory used by the library loader.

**Throws:**
- UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.

**See Also:**
- getLibraryDirectory()

---

#### public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception

Allows the m-let to perform any operations it needs before
being registered in the MBean server. If the ObjectName is
null, the m-let provides a default name for its registration
<defaultDomain>:type=MLet

**Specified by:**
- preRegister

in interface

MBeanRegistration

**Parameters:**
- server

- The MBean server in which the m-let will be registered.
- name

- The object name of the m-let.

**Returns:**
- The name of the m-let registered.

**Throws:**
- Exception

- This exception should be caught by the MBean server and re-thrown
as an MBeanRegistrationException.

---

#### public void postRegister​(
Boolean
registrationDone)

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

**Specified by:**
- postRegister

in interface

MBeanRegistration

**Parameters:**
- registrationDone

- Indicates whether or not the m-let has
been successfully registered in the MBean server. The value
false means that either the registration phase has failed.

---

#### public void preDeregister()
throws
Exception

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

**Specified by:**
- preDeregister

in interface

MBeanRegistration

**Throws:**
- Exception

- This exception should be caught
by the MBean server and re-thrown as an
MBeanRegistrationException.

---

#### public void postDeregister()

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

**Specified by:**
- postDeregister

in interface

MBeanRegistration

---

#### public void writeExternal​(
ObjectOutput
out)
throws
IOException
,

UnsupportedOperationException

Save this MLet's contents to the given

ObjectOutput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the written data.

The format of the written data is not specified, but if
an implementation supports

writeExternal(java.io.ObjectOutput)

it must
also support

readExternal(java.io.ObjectInput)

in such a way that what is
written by the former can be read by the latter.

**Specified by:**
- writeExternal

in interface

Externalizable

**Parameters:**
- out

- The object output stream to write to.

**Throws:**
- IOException

- If a problem occurred while writing.
- UnsupportedOperationException

- If this
implementation does not support this operation.

---

#### public void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException
,

UnsupportedOperationException

Restore this MLet's contents from the given

ObjectInput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the read data.

The format of the read data is not specified, but if an
implementation supports

readExternal(java.io.ObjectInput)

it must also
support

writeExternal(java.io.ObjectOutput)

in such a way that what is
written by the latter can be read by the former.

**Specified by:**
- readExternal

in interface

Externalizable

**Parameters:**
- in

- The object input stream to read from.

**Throws:**
- IOException

- if a problem occurred while reading.
- ClassNotFoundException

- if the class for the object
being restored cannot be found.
- UnsupportedOperationException

- if this
implementation does not support this operation.

---

#### public
Class
<?> loadClass​(
String
name,

ClassLoaderRepository
clr)
throws
ClassNotFoundException

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs. The given
ClassLoaderRepository can be null, in which case a

ClassNotFoundException

occurs immediately if the class is not
found in this MLet's URLs.

**Parameters:**
- name

- The name of the class we want to load.
- clr

- The ClassLoaderRepository that will be used to search
for the given class, if it is not found in this
ClassLoader. May be null.

**Returns:**
- The resulting Class object.

**Throws:**
- ClassNotFoundException

- The specified class could not be
found in this ClassLoader nor in the given
ClassLoaderRepository.

---

#### protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException

This is the main method for class loaders that is being redefined.

**Overrides:**
- findClass

in class

URLClassLoader

**Parameters:**
- name

- The name of the class.

**Returns:**
- The resulting Class object.

**Throws:**
- ClassNotFoundException

- The specified class could not be
found.

---

#### protected
String
findLibrary​(
String
libname)

Returns the absolute path name of a native library. The VM
invokes this method to locate the native libraries that belong
to classes loaded with this class loader. Libraries are
searched in the JAR files using first just the native library
name and if not found the native library name together with
the architecture-specific path name
(

OSName/OSArch/OSVersion/lib/nativelibname

), i.e.

the library stat on Solaris SPARC 5.7 will be searched in the JAR file as:

- libstat.so

SunOS/sparc/5.7/lib/libstat.so

the library stat on Windows NT 4.0 will be searched in the JAR file as:

- stat.dll

WindowsNT/x86/4.0/lib/stat.dll

More specifically, let

nativelibname

be the result of

System.mapLibraryName

(libname)

. Then the following names are
searched in the JAR files, in order:

nativelibname

<os.name>/<os.arch>/<os.version>/lib/

nativelibname

where

<X>

means

System.getProperty(X)

with any
spaces in the result removed, and

/

stands for the
file separator character (

File.separator

).

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

**Overrides:**
- findLibrary

in class

ClassLoader

**Parameters:**
- libname

- The library name.

**Returns:**
- The absolute path of the native library.

**See Also:**
- System.loadLibrary(String)

,

System.mapLibraryName(String)

---

#### protected
URL
check​(
String
version,

URL
codebase,

String
jarfile,

MLetContent
mlet)
throws
Exception

This method is to be overridden when extending this service to
support caching and versioning. It is called from

getMBeansFromURL

when the version,
codebase, and jarfile have been extracted from the MLet file,
and can be used to verify that it is all right to load the
given MBean, or to replace the given URL with a different one.

The default implementation of this method returns

codebase

unchanged.

**Parameters:**
- version

- The version number of the

.jar

file stored locally.
- codebase

- The base URL of the remote

.jar

file.
- jarfile

- The name of the

.jar

file to be loaded.
- mlet

- The

MLetContent

instance that
represents the

MLET

tag.

**Returns:**
- the codebase to use for the loaded MBean. The returned
value should not be null.

**Throws:**
- Exception

- if the MBean is not to be loaded for some
reason. The exception will be added to the set returned by

getMBeansFromURL

.

---

### Additional Sections

#### Class MLet

java.lang.Object

- java.lang.ClassLoader
- - java.security.SecureClassLoader
- - java.net.URLClassLoader
- - javax.management.loading.MLet

java.lang.ClassLoader

- java.security.SecureClassLoader
- - java.net.URLClassLoader
- - javax.management.loading.MLet

java.security.SecureClassLoader

- java.net.URLClassLoader
- - javax.management.loading.MLet

java.net.URLClassLoader

- javax.management.loading.MLet

javax.management.loading.MLet

**All Implemented Interfaces:** Closeable

,

Externalizable

,

Serializable

,

AutoCloseable

,

MLetMBean

,

MBeanRegistration

**Direct Known Subclasses:** PrivateMLet

```java
public class
MLet

extends
URLClassLoader

implements
MLetMBean
,
MBeanRegistration
,
Externalizable
```

Allows you to instantiate and register one or several MBeans in the MBean server
coming from a remote URL. M-let is a shortcut for management applet. The m-let service does this
by loading an m-let text file, which specifies information on the MBeans to be obtained.
The information on each MBean is specified in a single instance of a tag, called the MLET tag.
The location of the m-let text file is specified by a URL.

The

MLET

tag has the following syntax:

<

MLET

CODE =

class

| OBJECT =

serfile

ARCHIVE = "

archiveList

"

[CODEBASE =

codebaseURL

]

[NAME =

mbeanname

]

[VERSION =

version

]

>

[

arglist

]

<

/MLET

>

where:

**CODE = class:** This attribute specifies the full Java class name, including package name, of the MBean to be obtained.
The compiled

.class

file of the MBean must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. Either

CODE

or

OBJECT

must be present.
**OBJECT = serfile:** This attribute specifies the

.ser

file that contains a serialized representation of the MBean to be obtained.
This file must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. If the

.jar

file contains a directory hierarchy, specify the path of the file within this hierarchy. Otherwise a match will not be found. Either

CODE

or

OBJECT

must be present.
**ARCHIVE = " archiveList ":** This mandatory attribute specifies one or more

.jar

files
containing MBeans or other resources used by
the MBean to be obtained. One of the

.jar

files must contain the file specified by the

CODE

or

OBJECT

attribute.
If archivelist contains more than one file:

- Each file must be separated from the one that follows it by a comma (,).

archivelist

must be enclosed in double quote marks.

All

.jar

files in

archivelist

must be stored in the directory specified by the code base URL.
**CODEBASE = codebaseURL:** This optional attribute specifies the code base URL of the MBean to be obtained. It identifies the directory that contains
the

.jar

files specified by the

ARCHIVE

attribute. Specify this attribute only if the

.jar

files are not in the same
directory as the m-let text file. If this attribute is not specified, the base URL of the m-let text file is used.
**NAME = mbeanname:** This optional attribute specifies the object name to be assigned to the
MBean instance when the m-let service registers it. If

mbeanname

starts with the colon character (:), the domain
part of the object name is the default domain of the MBean server,
as returned by

MBeanServerConnection.getDefaultDomain()

.
**VERSION = version:** This optional attribute specifies the version number of the MBean and
associated

.jar

files to be obtained. This version number can
be used to specify that the

.jar

files are loaded from the
server to update those stored locally in the cache the next time the m-let
text file is loaded.

version

must be a series of non-negative
decimal integers each separated by a period from the one that precedes it.
**arglist:** This optional attribute specifies a list of one or more parameters for the
MBean to be instantiated. This list describes the parameters to be passed the MBean's constructor.
Use the following syntax to specify each item in

arglist

:

**< ARG TYPE= argumentType VALUE= value >:** where:

- argumentType

is the type of the argument that will be passed as parameter to the MBean's constructor.

The arguments' type in the argument list should be a Java primitive type or a Java basic type
(

java.lang.Boolean, java.lang.Byte, java.lang.Short, java.lang.Long, java.lang.Integer, java.lang.Float, java.lang.Double, java.lang.String

).

When an m-let text file is loaded, an
instance of each MBean specified in the file is created and registered.

The m-let service extends the

java.net.URLClassLoader

and can be used to load remote classes
and jar files in the VM of the agent.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

**Since:** 1.5
**See Also:** Serialized Form

public class

MLet

extends

URLClassLoader

implements

MLetMBean

,

MBeanRegistration

,

Externalizable

Allows you to instantiate and register one or several MBeans in the MBean server
coming from a remote URL. M-let is a shortcut for management applet. The m-let service does this
by loading an m-let text file, which specifies information on the MBeans to be obtained.
The information on each MBean is specified in a single instance of a tag, called the MLET tag.
The location of the m-let text file is specified by a URL.

The

MLET

tag has the following syntax:

<

MLET

CODE =

class

| OBJECT =

serfile

ARCHIVE = "

archiveList

"

[CODEBASE =

codebaseURL

]

[NAME =

mbeanname

]

[VERSION =

version

]

>

[

arglist

]

<

/MLET

>

where:

**CODE = class:** This attribute specifies the full Java class name, including package name, of the MBean to be obtained.
The compiled

.class

file of the MBean must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. Either

CODE

or

OBJECT

must be present.
**OBJECT = serfile:** This attribute specifies the

.ser

file that contains a serialized representation of the MBean to be obtained.
This file must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. If the

.jar

file contains a directory hierarchy, specify the path of the file within this hierarchy. Otherwise a match will not be found. Either

CODE

or

OBJECT

must be present.
**ARCHIVE = " archiveList ":** This mandatory attribute specifies one or more

.jar

files
containing MBeans or other resources used by
the MBean to be obtained. One of the

.jar

files must contain the file specified by the

CODE

or

OBJECT

attribute.
If archivelist contains more than one file:

- Each file must be separated from the one that follows it by a comma (,).

archivelist

must be enclosed in double quote marks.

All

.jar

files in

archivelist

must be stored in the directory specified by the code base URL.
**CODEBASE = codebaseURL:** This optional attribute specifies the code base URL of the MBean to be obtained. It identifies the directory that contains
the

.jar

files specified by the

ARCHIVE

attribute. Specify this attribute only if the

.jar

files are not in the same
directory as the m-let text file. If this attribute is not specified, the base URL of the m-let text file is used.
**NAME = mbeanname:** This optional attribute specifies the object name to be assigned to the
MBean instance when the m-let service registers it. If

mbeanname

starts with the colon character (:), the domain
part of the object name is the default domain of the MBean server,
as returned by

MBeanServerConnection.getDefaultDomain()

.
**VERSION = version:** This optional attribute specifies the version number of the MBean and
associated

.jar

files to be obtained. This version number can
be used to specify that the

.jar

files are loaded from the
server to update those stored locally in the cache the next time the m-let
text file is loaded.

version

must be a series of non-negative
decimal integers each separated by a period from the one that precedes it.
**arglist:** This optional attribute specifies a list of one or more parameters for the
MBean to be instantiated. This list describes the parameters to be passed the MBean's constructor.
Use the following syntax to specify each item in

arglist

:

**< ARG TYPE= argumentType VALUE= value >:** where:

- argumentType

is the type of the argument that will be passed as parameter to the MBean's constructor.

The arguments' type in the argument list should be a Java primitive type or a Java basic type
(

java.lang.Boolean, java.lang.Byte, java.lang.Short, java.lang.Long, java.lang.Integer, java.lang.Float, java.lang.Double, java.lang.String

).

When an m-let text file is loaded, an
instance of each MBean specified in the file is created and registered.

The m-let service extends the

java.net.URLClassLoader

and can be used to load remote classes
and jar files in the VM of the agent.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

The

MLET

tag has the following syntax:

<

MLET

CODE =

class

| OBJECT =

serfile

ARCHIVE = "

archiveList

"

[CODEBASE =

codebaseURL

]

[NAME =

mbeanname

]

[VERSION =

version

]

>

[

arglist

]

<

/MLET

>

where:

**CODE = class:** This attribute specifies the full Java class name, including package name, of the MBean to be obtained.
The compiled

.class

file of the MBean must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. Either

CODE

or

OBJECT

must be present.
**OBJECT = serfile:** This attribute specifies the

.ser

file that contains a serialized representation of the MBean to be obtained.
This file must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. If the

.jar

file contains a directory hierarchy, specify the path of the file within this hierarchy. Otherwise a match will not be found. Either

CODE

or

OBJECT

must be present.
**ARCHIVE = " archiveList ":** This mandatory attribute specifies one or more

.jar

files
containing MBeans or other resources used by
the MBean to be obtained. One of the

.jar

files must contain the file specified by the

CODE

or

OBJECT

attribute.
If archivelist contains more than one file:

- Each file must be separated from the one that follows it by a comma (,).

archivelist

must be enclosed in double quote marks.

All

.jar

files in

archivelist

must be stored in the directory specified by the code base URL.
**CODEBASE = codebaseURL:** This optional attribute specifies the code base URL of the MBean to be obtained. It identifies the directory that contains
the

.jar

files specified by the

ARCHIVE

attribute. Specify this attribute only if the

.jar

files are not in the same
directory as the m-let text file. If this attribute is not specified, the base URL of the m-let text file is used.
**NAME = mbeanname:** This optional attribute specifies the object name to be assigned to the
MBean instance when the m-let service registers it. If

mbeanname

starts with the colon character (:), the domain
part of the object name is the default domain of the MBean server,
as returned by

MBeanServerConnection.getDefaultDomain()

.
**VERSION = version:** This optional attribute specifies the version number of the MBean and
associated

.jar

files to be obtained. This version number can
be used to specify that the

.jar

files are loaded from the
server to update those stored locally in the cache the next time the m-let
text file is loaded.

version

must be a series of non-negative
decimal integers each separated by a period from the one that precedes it.
**arglist:** This optional attribute specifies a list of one or more parameters for the
MBean to be instantiated. This list describes the parameters to be passed the MBean's constructor.
Use the following syntax to specify each item in

arglist

:

**< ARG TYPE= argumentType VALUE= value >:** where:

- argumentType

is the type of the argument that will be passed as parameter to the MBean's constructor.

The arguments' type in the argument list should be a Java primitive type or a Java basic type
(

java.lang.Boolean, java.lang.Byte, java.lang.Short, java.lang.Long, java.lang.Integer, java.lang.Float, java.lang.Double, java.lang.String

).

When an m-let text file is loaded, an
instance of each MBean specified in the file is created and registered.

The m-let service extends the

java.net.URLClassLoader

and can be used to load remote classes
and jar files in the VM of the agent.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

<

MLET

CODE =

class

| OBJECT =

serfile

ARCHIVE = "

archiveList

"

[CODEBASE =

codebaseURL

]

[NAME =

mbeanname

]

[VERSION =

version

]

>

[

arglist

]

<

/MLET

>

where:

**CODE = class:** This attribute specifies the full Java class name, including package name, of the MBean to be obtained.
The compiled

.class

file of the MBean must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. Either

CODE

or

OBJECT

must be present.
**OBJECT = serfile:** This attribute specifies the

.ser

file that contains a serialized representation of the MBean to be obtained.
This file must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. If the

.jar

file contains a directory hierarchy, specify the path of the file within this hierarchy. Otherwise a match will not be found. Either

CODE

or

OBJECT

must be present.
**ARCHIVE = " archiveList ":** This mandatory attribute specifies one or more

.jar

files
containing MBeans or other resources used by
the MBean to be obtained. One of the

.jar

files must contain the file specified by the

CODE

or

OBJECT

attribute.
If archivelist contains more than one file:

- Each file must be separated from the one that follows it by a comma (,).

archivelist

must be enclosed in double quote marks.

All

.jar

files in

archivelist

must be stored in the directory specified by the code base URL.
**CODEBASE = codebaseURL:** This optional attribute specifies the code base URL of the MBean to be obtained. It identifies the directory that contains
the

.jar

files specified by the

ARCHIVE

attribute. Specify this attribute only if the

.jar

files are not in the same
directory as the m-let text file. If this attribute is not specified, the base URL of the m-let text file is used.
**NAME = mbeanname:** This optional attribute specifies the object name to be assigned to the
MBean instance when the m-let service registers it. If

mbeanname

starts with the colon character (:), the domain
part of the object name is the default domain of the MBean server,
as returned by

MBeanServerConnection.getDefaultDomain()

.
**VERSION = version:** This optional attribute specifies the version number of the MBean and
associated

.jar

files to be obtained. This version number can
be used to specify that the

.jar

files are loaded from the
server to update those stored locally in the cache the next time the m-let
text file is loaded.

version

must be a series of non-negative
decimal integers each separated by a period from the one that precedes it.
**arglist:** This optional attribute specifies a list of one or more parameters for the
MBean to be instantiated. This list describes the parameters to be passed the MBean's constructor.
Use the following syntax to specify each item in

arglist

:

**< ARG TYPE= argumentType VALUE= value >:** where:

- argumentType

is the type of the argument that will be passed as parameter to the MBean's constructor.

The arguments' type in the argument list should be a Java primitive type or a Java basic type
(

java.lang.Boolean, java.lang.Byte, java.lang.Short, java.lang.Long, java.lang.Integer, java.lang.Float, java.lang.Double, java.lang.String

).

When an m-let text file is loaded, an
instance of each MBean specified in the file is created and registered.

The m-let service extends the

java.net.URLClassLoader

and can be used to load remote classes
and jar files in the VM of the agent.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

where:

**CODE = class:** This attribute specifies the full Java class name, including package name, of the MBean to be obtained.
The compiled

.class

file of the MBean must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. Either

CODE

or

OBJECT

must be present.
**OBJECT = serfile:** This attribute specifies the

.ser

file that contains a serialized representation of the MBean to be obtained.
This file must be contained in one of the

.jar

files specified by the

ARCHIVE

attribute. If the

.jar

file contains a directory hierarchy, specify the path of the file within this hierarchy. Otherwise a match will not be found. Either

CODE

or

OBJECT

must be present.
**ARCHIVE = " archiveList ":** This mandatory attribute specifies one or more

.jar

files
containing MBeans or other resources used by
the MBean to be obtained. One of the

.jar

files must contain the file specified by the

CODE

or

OBJECT

attribute.
If archivelist contains more than one file:

- Each file must be separated from the one that follows it by a comma (,).

archivelist

must be enclosed in double quote marks.

All

.jar

files in

archivelist

must be stored in the directory specified by the code base URL.
**CODEBASE = codebaseURL:** This optional attribute specifies the code base URL of the MBean to be obtained. It identifies the directory that contains
the

.jar

files specified by the

ARCHIVE

attribute. Specify this attribute only if the

.jar

files are not in the same
directory as the m-let text file. If this attribute is not specified, the base URL of the m-let text file is used.
**NAME = mbeanname:** This optional attribute specifies the object name to be assigned to the
MBean instance when the m-let service registers it. If

mbeanname

starts with the colon character (:), the domain
part of the object name is the default domain of the MBean server,
as returned by

MBeanServerConnection.getDefaultDomain()

.
**VERSION = version:** This optional attribute specifies the version number of the MBean and
associated

.jar

files to be obtained. This version number can
be used to specify that the

.jar

files are loaded from the
server to update those stored locally in the cache the next time the m-let
text file is loaded.

version

must be a series of non-negative
decimal integers each separated by a period from the one that precedes it.
**arglist:** This optional attribute specifies a list of one or more parameters for the
MBean to be instantiated. This list describes the parameters to be passed the MBean's constructor.
Use the following syntax to specify each item in

arglist

:

**< ARG TYPE= argumentType VALUE= value >:** where:

- argumentType

is the type of the argument that will be passed as parameter to the MBean's constructor.

The arguments' type in the argument list should be a Java primitive type or a Java basic type
(

java.lang.Boolean, java.lang.Byte, java.lang.Short, java.lang.Long, java.lang.Integer, java.lang.Float, java.lang.Double, java.lang.String

).

When an m-let text file is loaded, an
instance of each MBean specified in the file is created and registered.

The m-let service extends the

java.net.URLClassLoader

and can be used to load remote classes
and jar files in the VM of the agent.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

Each file must be separated from the one that follows it by a comma (,).

archivelist

must be enclosed in double quote marks.

argumentType

is the type of the argument that will be passed as parameter to the MBean's constructor.

The arguments' type in the argument list should be a Java primitive type or a Java basic type
(

java.lang.Boolean, java.lang.Byte, java.lang.Short, java.lang.Long, java.lang.Integer, java.lang.Float, java.lang.Double, java.lang.String

).

The m-let service extends the

java.net.URLClassLoader

and can be used to load remote classes
and jar files in the VM of the agent.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

Note -

The

MLet

class loader uses the

MBeanServerFactory.getClassLoaderRepository(javax.management.MBeanServer)

to load classes that could not be found in the loaded jar files.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MLet

()

Constructs a new MLet using the default delegation parent ClassLoader.

MLet

​(

URL

[] urls)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader.

MLet

​(

URL

[] urls,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader.

MLet

​(

URL

[] urls,

ClassLoader

parent)

Constructs a new MLet for the given URLs.

MLet

​(

URL

[] urls,

ClassLoader

parent,
boolean delegateToCLR)

Constructs a new MLet for the given URLs.

MLet

​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory.

MLet

​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addURL

​(

String

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

void

addURL

​(

URL

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

protected

URL

check

​(

String

version,

URL

codebase,

String

jarfile,

MLetContent

mlet)

This method is to be overridden when extending this service to
support caching and versioning.

protected

Class

<?>

findClass

​(

String

name)

This is the main method for class loaders that is being redefined.

protected

String

findLibrary

​(

String

libname)

Returns the absolute path name of a native library.

String

getLibraryDirectory

()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

Set

<

Object

>

getMBeansFromURL

​(

String

url)

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server.

Set

<

Object

>

getMBeansFromURL

​(

URL

url)

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server.

URL

[]

getURLs

()

Returns the search path of URLs for loading classes and resources.

Class

<?>

loadClass

​(

String

name,

ClassLoaderRepository

clr)

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs.

void

postDeregister

()

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the m-let to perform any operations it needs before
being registered in the MBean server.

void

readExternal

​(

ObjectInput

in)

Restore this MLet's contents from the given

ObjectInput

.

void

setLibraryDirectory

​(

String

libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

void

writeExternal

​(

ObjectOutput

out)

Save this MLet's contents to the given

ObjectOutput

.

- Methods declared in class java.net.

URLClassLoader

close

,

definePackage

,

findResource

,

findResources

,

getPermissions

,

getResourceAsStream

,

newInstance

,

newInstance

- Methods declared in class java.security.

SecureClassLoader

defineClass

,

defineClass

- Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findLoadedClass

,

findResource

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

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

- Methods declared in interface javax.management.loading.

MLetMBean

getResource

,

getResourceAsStream

,

getResources

Constructor Summary

Constructors

Constructor

Description

MLet

()

Constructs a new MLet using the default delegation parent ClassLoader.

MLet

​(

URL

[] urls)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader.

MLet

​(

URL

[] urls,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader.

MLet

​(

URL

[] urls,

ClassLoader

parent)

Constructs a new MLet for the given URLs.

MLet

​(

URL

[] urls,

ClassLoader

parent,
boolean delegateToCLR)

Constructs a new MLet for the given URLs.

MLet

​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory.

MLet

​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory.

---

#### Constructor Summary

Constructs a new MLet using the default delegation parent ClassLoader.

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader.

Constructs a new MLet for the given URLs.

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addURL

​(

String

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

void

addURL

​(

URL

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

protected

URL

check

​(

String

version,

URL

codebase,

String

jarfile,

MLetContent

mlet)

This method is to be overridden when extending this service to
support caching and versioning.

protected

Class

<?>

findClass

​(

String

name)

This is the main method for class loaders that is being redefined.

protected

String

findLibrary

​(

String

libname)

Returns the absolute path name of a native library.

String

getLibraryDirectory

()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

Set

<

Object

>

getMBeansFromURL

​(

String

url)

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server.

Set

<

Object

>

getMBeansFromURL

​(

URL

url)

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server.

URL

[]

getURLs

()

Returns the search path of URLs for loading classes and resources.

Class

<?>

loadClass

​(

String

name,

ClassLoaderRepository

clr)

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs.

void

postDeregister

()

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the m-let to perform any operations it needs before
being registered in the MBean server.

void

readExternal

​(

ObjectInput

in)

Restore this MLet's contents from the given

ObjectInput

.

void

setLibraryDirectory

​(

String

libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

void

writeExternal

​(

ObjectOutput

out)

Save this MLet's contents to the given

ObjectOutput

.

- Methods declared in class java.net.

URLClassLoader

close

,

definePackage

,

findResource

,

findResources

,

getPermissions

,

getResourceAsStream

,

newInstance

,

newInstance

- Methods declared in class java.security.

SecureClassLoader

defineClass

,

defineClass

- Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findLoadedClass

,

findResource

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

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

- Methods declared in interface javax.management.loading.

MLetMBean

getResource

,

getResourceAsStream

,

getResources

---

#### Method Summary

Appends the specified URL to the list of URLs to search for classes and
resources.

This method is to be overridden when extending this service to
support caching and versioning.

This is the main method for class loaders that is being redefined.

Returns the absolute path name of a native library.

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server.

Returns the search path of URLs for loading classes and resources.

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs.

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

Allows the m-let to perform any operations it needs before
being registered in the MBean server.

Restore this MLet's contents from the given

ObjectInput

.

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

Save this MLet's contents to the given

ObjectOutput

.

Methods declared in class java.net.

URLClassLoader

close

,

definePackage

,

findResource

,

findResources

,

getPermissions

,

getResourceAsStream

,

newInstance

,

newInstance

---

#### Methods declared in class java.net. URLClassLoader

Methods declared in class java.security.

SecureClassLoader

defineClass

,

defineClass

---

#### Methods declared in class java.security. SecureClassLoader

Methods declared in class java.lang.

ClassLoader

clearAssertionStatus

,

defineClass

,

defineClass

,

defineClass

,

defineClass

,

definePackage

,

findClass

,

findLoadedClass

,

findResource

,

findSystemClass

,

getClassLoadingLock

,

getDefinedPackage

,

getDefinedPackages

,

getName

,

getPackage

,

getPackages

,

getParent

,

getPlatformClassLoader

,

getResource

,

getResources

,

getSystemClassLoader

,

getSystemResource

,

getSystemResourceAsStream

,

getSystemResources

,

getUnnamedModule

,

isRegisteredAsParallelCapable

,

loadClass

,

loadClass

,

registerAsParallelCapable

,

resolveClass

,

resources

,

setClassAssertionStatus

,

setDefaultAssertionStatus

,

setPackageAssertionStatus

,

setSigners

---

#### Methods declared in class java.lang. ClassLoader

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

Methods declared in interface javax.management.loading.

MLetMBean

getResource

,

getResourceAsStream

,

getResources

---

#### Methods declared in interface javax.management.loading. MLetMBean

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MLet

```java
public MLet()
```

Constructs a new MLet using the default delegation parent ClassLoader.

- MLet

```java
public MLet​(
URL
[] urls)
```

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent)
```

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory)
```

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.

- MLet

```java
public MLet​(
URL
[] urls,
boolean delegateToCLR)
```

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)
```

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)
```

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

============ METHOD DETAIL ==========

- Method Detail

- addURL

```java
public void addURL​(
URL
url)
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:** addURL

in interface

MLetMBean
**Overrides:** addURL

in class

URLClassLoader
**Parameters:** url

- the URL to be added to the search path of URLs

- addURL

```java
public void addURL​(
String
url)
throws
ServiceNotFoundException
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:** addURL

in interface

MLetMBean
**Parameters:** url

- the URL to add.
**Throws:** ServiceNotFoundException

- The specified URL is malformed.

- getURLs

```java
public
URL
[] getURLs()
```

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Specified by:** getURLs

in interface

MLetMBean
**Overrides:** getURLs

in class

URLClassLoader
**Returns:** the search path of URLs for loading classes and resources.

- getMBeansFromURL

```java
public
Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:** getMBeansFromURL

in interface

MLetMBean
**Parameters:** url

- The URL of the text file to be loaded as URL object.
**Returns:** A set containing one entry per MLET tag in the m-let text file loaded.
Each entry specifies either the ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be created.
**Throws:** ServiceNotFoundException

- One of the following errors has occurred: The m-let text file does
not contain an MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the value of url is
null.
**Throws:** IllegalStateException

- MLet MBean is not registered with an MBeanServer.

- getMBeansFromURL

```java
public
Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:** getMBeansFromURL

in interface

MLetMBean
**Parameters:** url

- The URL of the text file to be loaded as String object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following
errors has occurred: The m-let text file does not contain an
MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the url is
malformed.
**Throws:** IllegalStateException

- MLet MBean is not registered
with an MBeanServer.

- getLibraryDirectory

```java
public
String
getLibraryDirectory()
```

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Specified by:** getLibraryDirectory

in interface

MLetMBean
**Returns:** The current directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** setLibraryDirectory(java.lang.String)

- setLibraryDirectory

```java
public void setLibraryDirectory​(
String
libdir)
```

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Specified by:** setLibraryDirectory

in interface

MLetMBean
**Parameters:** libdir

- The directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** getLibraryDirectory()

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the m-let to perform any operations it needs before
being registered in the MBean server. If the ObjectName is
null, the m-let provides a default name for its registration
<defaultDomain>:type=MLet

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the m-let will be registered.
**Parameters:** name

- The object name of the m-let.
**Returns:** The name of the m-let registered.
**Throws:** Exception

- This exception should be caught by the MBean server and re-thrown
as an MBeanRegistrationException.

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the m-let has
been successfully registered in the MBean server. The value
false means that either the registration phase has failed.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- This exception should be caught
by the MBean server and re-thrown as an
MBeanRegistrationException.

- postDeregister

```java
public void postDeregister()
```

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

**Specified by:** postDeregister

in interface

MBeanRegistration

- writeExternal

```java
public void writeExternal​(
ObjectOutput
out)
throws
IOException
,

UnsupportedOperationException
```

Save this MLet's contents to the given

ObjectOutput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the written data.

The format of the written data is not specified, but if
an implementation supports

writeExternal(java.io.ObjectOutput)

it must
also support

readExternal(java.io.ObjectInput)

in such a way that what is
written by the former can be read by the latter.

**Specified by:** writeExternal

in interface

Externalizable
**Parameters:** out

- The object output stream to write to.
**Throws:** IOException

- If a problem occurred while writing.
**Throws:** UnsupportedOperationException

- If this
implementation does not support this operation.

- readExternal

```java
public void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException
,

UnsupportedOperationException
```

Restore this MLet's contents from the given

ObjectInput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the read data.

The format of the read data is not specified, but if an
implementation supports

readExternal(java.io.ObjectInput)

it must also
support

writeExternal(java.io.ObjectOutput)

in such a way that what is
written by the latter can be read by the former.

**Specified by:** readExternal

in interface

Externalizable
**Parameters:** in

- The object input stream to read from.
**Throws:** IOException

- if a problem occurred while reading.
**Throws:** ClassNotFoundException

- if the class for the object
being restored cannot be found.
**Throws:** UnsupportedOperationException

- if this
implementation does not support this operation.

- loadClass

```java
public
Class
<?> loadClass​(
String
name,

ClassLoaderRepository
clr)
throws
ClassNotFoundException
```

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs. The given
ClassLoaderRepository can be null, in which case a

ClassNotFoundException

occurs immediately if the class is not
found in this MLet's URLs.

**Parameters:** name

- The name of the class we want to load.
**Parameters:** clr

- The ClassLoaderRepository that will be used to search
for the given class, if it is not found in this
ClassLoader. May be null.
**Returns:** The resulting Class object.
**Throws:** ClassNotFoundException

- The specified class could not be
found in this ClassLoader nor in the given
ClassLoaderRepository.

- findClass

```java
protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

This is the main method for class loaders that is being redefined.

**Overrides:** findClass

in class

URLClassLoader
**Parameters:** name

- The name of the class.
**Returns:** The resulting Class object.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

- findLibrary

```java
protected
String
findLibrary​(
String
libname)
```

Returns the absolute path name of a native library. The VM
invokes this method to locate the native libraries that belong
to classes loaded with this class loader. Libraries are
searched in the JAR files using first just the native library
name and if not found the native library name together with
the architecture-specific path name
(

OSName/OSArch/OSVersion/lib/nativelibname

), i.e.

the library stat on Solaris SPARC 5.7 will be searched in the JAR file as:

- libstat.so

SunOS/sparc/5.7/lib/libstat.so

the library stat on Windows NT 4.0 will be searched in the JAR file as:

- stat.dll

WindowsNT/x86/4.0/lib/stat.dll

More specifically, let

nativelibname

be the result of

System.mapLibraryName

(libname)

. Then the following names are
searched in the JAR files, in order:

nativelibname

<os.name>/<os.arch>/<os.version>/lib/

nativelibname

where

<X>

means

System.getProperty(X)

with any
spaces in the result removed, and

/

stands for the
file separator character (

File.separator

).

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

**Overrides:** findLibrary

in class

ClassLoader
**Parameters:** libname

- The library name.
**Returns:** The absolute path of the native library.
**See Also:** System.loadLibrary(String)

,

System.mapLibraryName(String)

- check

```java
protected
URL
check​(
String
version,

URL
codebase,

String
jarfile,

MLetContent
mlet)
throws
Exception
```

This method is to be overridden when extending this service to
support caching and versioning. It is called from

getMBeansFromURL

when the version,
codebase, and jarfile have been extracted from the MLet file,
and can be used to verify that it is all right to load the
given MBean, or to replace the given URL with a different one.

The default implementation of this method returns

codebase

unchanged.

**Parameters:** version

- The version number of the

.jar

file stored locally.
**Parameters:** codebase

- The base URL of the remote

.jar

file.
**Parameters:** jarfile

- The name of the

.jar

file to be loaded.
**Parameters:** mlet

- The

MLetContent

instance that
represents the

MLET

tag.
**Returns:** the codebase to use for the loaded MBean. The returned
value should not be null.
**Throws:** Exception

- if the MBean is not to be loaded for some
reason. The exception will be added to the set returned by

getMBeansFromURL

.

Constructor Detail

- MLet

```java
public MLet()
```

Constructs a new MLet using the default delegation parent ClassLoader.

- MLet

```java
public MLet​(
URL
[] urls)
```

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent)
```

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory)
```

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.

- MLet

```java
public MLet​(
URL
[] urls,
boolean delegateToCLR)
```

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)
```

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

- MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)
```

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### Constructor Detail

MLet

```java
public MLet()
```

Constructs a new MLet using the default delegation parent ClassLoader.

---

#### MLet

public MLet()

Constructs a new MLet using the default delegation parent ClassLoader.

MLet

```java
public MLet​(
URL
[] urls)
```

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.

---

#### MLet

public MLet​(

URL

[] urls)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent)
```

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.

---

#### MLet

public MLet​(

URL

[] urls,

ClassLoader

parent)

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory)
```

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.

---

#### MLet

public MLet​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

MLet

```java
public MLet​(
URL
[] urls,
boolean delegateToCLR)
```

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### MLet

public MLet​(

URL

[] urls,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs using the default
delegation parent ClassLoader. The URLs will be searched in
the order specified for classes and resources after first
searching in the parent class loader.

MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,
boolean delegateToCLR)
```

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### MLet

public MLet​(

URL

[] urls,

ClassLoader

parent,
boolean delegateToCLR)

Constructs a new MLet for the given URLs. The URLs will be
searched in the order specified for classes and resources
after first searching in the specified parent class loader.
The parent argument will be used as the parent class loader
for delegation.

MLet

```java
public MLet​(
URL
[] urls,

ClassLoader
parent,

URLStreamHandlerFactory
factory,
boolean delegateToCLR)
```

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

**Parameters:** urls

- The URLs from which to load classes and resources.
**Parameters:** parent

- The parent class loader for delegation.
**Parameters:** factory

- The URLStreamHandlerFactory to use when creating URLs.
**Parameters:** delegateToCLR

- True if, when a class is not found in
either the parent ClassLoader or the URLs, the MLet should delegate
to its containing MBeanServer's

ClassLoaderRepository

.

---

#### MLet

public MLet​(

URL

[] urls,

ClassLoader

parent,

URLStreamHandlerFactory

factory,
boolean delegateToCLR)

Constructs a new MLet for the specified URLs, parent class
loader, and URLStreamHandlerFactory. The parent argument will
be used as the parent class loader for delegation. The factory
argument will be used as the stream handler factory to obtain
protocol handlers when creating new URLs.

Method Detail

- addURL

```java
public void addURL​(
URL
url)
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:** addURL

in interface

MLetMBean
**Overrides:** addURL

in class

URLClassLoader
**Parameters:** url

- the URL to be added to the search path of URLs

- addURL

```java
public void addURL​(
String
url)
throws
ServiceNotFoundException
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:** addURL

in interface

MLetMBean
**Parameters:** url

- the URL to add.
**Throws:** ServiceNotFoundException

- The specified URL is malformed.

- getURLs

```java
public
URL
[] getURLs()
```

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Specified by:** getURLs

in interface

MLetMBean
**Overrides:** getURLs

in class

URLClassLoader
**Returns:** the search path of URLs for loading classes and resources.

- getMBeansFromURL

```java
public
Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:** getMBeansFromURL

in interface

MLetMBean
**Parameters:** url

- The URL of the text file to be loaded as URL object.
**Returns:** A set containing one entry per MLET tag in the m-let text file loaded.
Each entry specifies either the ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be created.
**Throws:** ServiceNotFoundException

- One of the following errors has occurred: The m-let text file does
not contain an MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the value of url is
null.
**Throws:** IllegalStateException

- MLet MBean is not registered with an MBeanServer.

- getMBeansFromURL

```java
public
Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:** getMBeansFromURL

in interface

MLetMBean
**Parameters:** url

- The URL of the text file to be loaded as String object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following
errors has occurred: The m-let text file does not contain an
MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the url is
malformed.
**Throws:** IllegalStateException

- MLet MBean is not registered
with an MBeanServer.

- getLibraryDirectory

```java
public
String
getLibraryDirectory()
```

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Specified by:** getLibraryDirectory

in interface

MLetMBean
**Returns:** The current directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** setLibraryDirectory(java.lang.String)

- setLibraryDirectory

```java
public void setLibraryDirectory​(
String
libdir)
```

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Specified by:** setLibraryDirectory

in interface

MLetMBean
**Parameters:** libdir

- The directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** getLibraryDirectory()

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the m-let to perform any operations it needs before
being registered in the MBean server. If the ObjectName is
null, the m-let provides a default name for its registration
<defaultDomain>:type=MLet

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the m-let will be registered.
**Parameters:** name

- The object name of the m-let.
**Returns:** The name of the m-let registered.
**Throws:** Exception

- This exception should be caught by the MBean server and re-thrown
as an MBeanRegistrationException.

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the m-let has
been successfully registered in the MBean server. The value
false means that either the registration phase has failed.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- This exception should be caught
by the MBean server and re-thrown as an
MBeanRegistrationException.

- postDeregister

```java
public void postDeregister()
```

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

**Specified by:** postDeregister

in interface

MBeanRegistration

- writeExternal

```java
public void writeExternal​(
ObjectOutput
out)
throws
IOException
,

UnsupportedOperationException
```

Save this MLet's contents to the given

ObjectOutput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the written data.

The format of the written data is not specified, but if
an implementation supports

writeExternal(java.io.ObjectOutput)

it must
also support

readExternal(java.io.ObjectInput)

in such a way that what is
written by the former can be read by the latter.

**Specified by:** writeExternal

in interface

Externalizable
**Parameters:** out

- The object output stream to write to.
**Throws:** IOException

- If a problem occurred while writing.
**Throws:** UnsupportedOperationException

- If this
implementation does not support this operation.

- readExternal

```java
public void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException
,

UnsupportedOperationException
```

Restore this MLet's contents from the given

ObjectInput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the read data.

The format of the read data is not specified, but if an
implementation supports

readExternal(java.io.ObjectInput)

it must also
support

writeExternal(java.io.ObjectOutput)

in such a way that what is
written by the latter can be read by the former.

**Specified by:** readExternal

in interface

Externalizable
**Parameters:** in

- The object input stream to read from.
**Throws:** IOException

- if a problem occurred while reading.
**Throws:** ClassNotFoundException

- if the class for the object
being restored cannot be found.
**Throws:** UnsupportedOperationException

- if this
implementation does not support this operation.

- loadClass

```java
public
Class
<?> loadClass​(
String
name,

ClassLoaderRepository
clr)
throws
ClassNotFoundException
```

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs. The given
ClassLoaderRepository can be null, in which case a

ClassNotFoundException

occurs immediately if the class is not
found in this MLet's URLs.

**Parameters:** name

- The name of the class we want to load.
**Parameters:** clr

- The ClassLoaderRepository that will be used to search
for the given class, if it is not found in this
ClassLoader. May be null.
**Returns:** The resulting Class object.
**Throws:** ClassNotFoundException

- The specified class could not be
found in this ClassLoader nor in the given
ClassLoaderRepository.

- findClass

```java
protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

This is the main method for class loaders that is being redefined.

**Overrides:** findClass

in class

URLClassLoader
**Parameters:** name

- The name of the class.
**Returns:** The resulting Class object.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

- findLibrary

```java
protected
String
findLibrary​(
String
libname)
```

Returns the absolute path name of a native library. The VM
invokes this method to locate the native libraries that belong
to classes loaded with this class loader. Libraries are
searched in the JAR files using first just the native library
name and if not found the native library name together with
the architecture-specific path name
(

OSName/OSArch/OSVersion/lib/nativelibname

), i.e.

the library stat on Solaris SPARC 5.7 will be searched in the JAR file as:

- libstat.so

SunOS/sparc/5.7/lib/libstat.so

the library stat on Windows NT 4.0 will be searched in the JAR file as:

- stat.dll

WindowsNT/x86/4.0/lib/stat.dll

More specifically, let

nativelibname

be the result of

System.mapLibraryName

(libname)

. Then the following names are
searched in the JAR files, in order:

nativelibname

<os.name>/<os.arch>/<os.version>/lib/

nativelibname

where

<X>

means

System.getProperty(X)

with any
spaces in the result removed, and

/

stands for the
file separator character (

File.separator

).

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

**Overrides:** findLibrary

in class

ClassLoader
**Parameters:** libname

- The library name.
**Returns:** The absolute path of the native library.
**See Also:** System.loadLibrary(String)

,

System.mapLibraryName(String)

- check

```java
protected
URL
check​(
String
version,

URL
codebase,

String
jarfile,

MLetContent
mlet)
throws
Exception
```

This method is to be overridden when extending this service to
support caching and versioning. It is called from

getMBeansFromURL

when the version,
codebase, and jarfile have been extracted from the MLet file,
and can be used to verify that it is all right to load the
given MBean, or to replace the given URL with a different one.

The default implementation of this method returns

codebase

unchanged.

**Parameters:** version

- The version number of the

.jar

file stored locally.
**Parameters:** codebase

- The base URL of the remote

.jar

file.
**Parameters:** jarfile

- The name of the

.jar

file to be loaded.
**Parameters:** mlet

- The

MLetContent

instance that
represents the

MLET

tag.
**Returns:** the codebase to use for the loaded MBean. The returned
value should not be null.
**Throws:** Exception

- if the MBean is not to be loaded for some
reason. The exception will be added to the set returned by

getMBeansFromURL

.

---

#### Method Detail

addURL

```java
public void addURL​(
URL
url)
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:** addURL

in interface

MLetMBean
**Overrides:** addURL

in class

URLClassLoader
**Parameters:** url

- the URL to be added to the search path of URLs

---

#### addURL

public void addURL​(

URL

url)

Appends the specified URL to the list of URLs to search for classes and
resources.

addURL

```java
public void addURL​(
String
url)
throws
ServiceNotFoundException
```

Appends the specified URL to the list of URLs to search for classes and
resources.

**Specified by:** addURL

in interface

MLetMBean
**Parameters:** url

- the URL to add.
**Throws:** ServiceNotFoundException

- The specified URL is malformed.

---

#### addURL

public void addURL​(

String

url)
throws

ServiceNotFoundException

Appends the specified URL to the list of URLs to search for classes and
resources.

getURLs

```java
public
URL
[] getURLs()
```

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

**Specified by:** getURLs

in interface

MLetMBean
**Overrides:** getURLs

in class

URLClassLoader
**Returns:** the search path of URLs for loading classes and resources.

---

#### getURLs

public

URL

[] getURLs()

Returns the search path of URLs for loading classes and resources.
This includes the original list of URLs specified to the constructor,
along with any URLs subsequently appended by the addURL() method.

getMBeansFromURL

```java
public
Set
<
Object
> getMBeansFromURL​(
URL
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:** getMBeansFromURL

in interface

MLetMBean
**Parameters:** url

- The URL of the text file to be loaded as URL object.
**Returns:** A set containing one entry per MLET tag in the m-let text file loaded.
Each entry specifies either the ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be created.
**Throws:** ServiceNotFoundException

- One of the following errors has occurred: The m-let text file does
not contain an MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the value of url is
null.
**Throws:** IllegalStateException

- MLet MBean is not registered with an MBeanServer.

---

#### getMBeansFromURL

public

Set

<

Object

> getMBeansFromURL​(

URL

url)
throws

ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

getMBeansFromURL

```java
public
Set
<
Object
> getMBeansFromURL​(
String
url)
throws
ServiceNotFoundException
```

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

**Specified by:** getMBeansFromURL

in interface

MLetMBean
**Parameters:** url

- The URL of the text file to be loaded as String object.
**Returns:** A set containing one entry per MLET tag in the m-let
text file loaded. Each entry specifies either the
ObjectInstance for the created MBean, or a throwable object
(that is, an error or an exception) if the MBean could not be
created.
**Throws:** ServiceNotFoundException

- One of the following
errors has occurred: The m-let text file does not contain an
MLET tag, the m-let text file is not found, a mandatory
attribute of the MLET tag is not specified, the url is
malformed.
**Throws:** IllegalStateException

- MLet MBean is not registered
with an MBeanServer.

---

#### getMBeansFromURL

public

Set

<

Object

> getMBeansFromURL​(

String

url)
throws

ServiceNotFoundException

Loads a text file containing MLET tags that define the MBeans to
be added to the MBean server. The location of the text file is specified by
a URL. The MBeans specified in the MLET file will be instantiated and
registered in the MBean server.

getLibraryDirectory

```java
public
String
getLibraryDirectory()
```

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

**Specified by:** getLibraryDirectory

in interface

MLetMBean
**Returns:** The current directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** setLibraryDirectory(java.lang.String)

---

#### getLibraryDirectory

public

String

getLibraryDirectory()

Gets the current directory used by the library loader for
storing native libraries before they are loaded into memory.

setLibraryDirectory

```java
public void setLibraryDirectory​(
String
libdir)
```

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

**Specified by:** setLibraryDirectory

in interface

MLetMBean
**Parameters:** libdir

- The directory used by the library loader.
**Throws:** UnsupportedOperationException

- if this implementation
does not support storing native libraries in this way.
**See Also:** getLibraryDirectory()

---

#### setLibraryDirectory

public void setLibraryDirectory​(

String

libdir)

Sets the directory used by the library loader for storing
native libraries before they are loaded into memory.

preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the m-let to perform any operations it needs before
being registered in the MBean server. If the ObjectName is
null, the m-let provides a default name for its registration
<defaultDomain>:type=MLet

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the m-let will be registered.
**Parameters:** name

- The object name of the m-let.
**Returns:** The name of the m-let registered.
**Throws:** Exception

- This exception should be caught by the MBean server and re-thrown
as an MBeanRegistrationException.

---

#### preRegister

public

ObjectName

preRegister​(

MBeanServer

server,

ObjectName

name)
throws

Exception

Allows the m-let to perform any operations it needs before
being registered in the MBean server. If the ObjectName is
null, the m-let provides a default name for its registration
<defaultDomain>:type=MLet

postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the m-let has
been successfully registered in the MBean server. The value
false means that either the registration phase has failed.

---

#### postRegister

public void postRegister​(

Boolean

registrationDone)

Allows the m-let to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- This exception should be caught
by the MBean server and re-thrown as an
MBeanRegistrationException.

---

#### preDeregister

public void preDeregister()
throws

Exception

Allows the m-let to perform any operations it needs before being unregistered
by the MBean server.

postDeregister

```java
public void postDeregister()
```

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

**Specified by:** postDeregister

in interface

MBeanRegistration

---

#### postDeregister

public void postDeregister()

Allows the m-let to perform any operations needed after having been
unregistered in the MBean server.

writeExternal

```java
public void writeExternal​(
ObjectOutput
out)
throws
IOException
,

UnsupportedOperationException
```

Save this MLet's contents to the given

ObjectOutput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the written data.

The format of the written data is not specified, but if
an implementation supports

writeExternal(java.io.ObjectOutput)

it must
also support

readExternal(java.io.ObjectInput)

in such a way that what is
written by the former can be read by the latter.

**Specified by:** writeExternal

in interface

Externalizable
**Parameters:** out

- The object output stream to write to.
**Throws:** IOException

- If a problem occurred while writing.
**Throws:** UnsupportedOperationException

- If this
implementation does not support this operation.

---

#### writeExternal

public void writeExternal​(

ObjectOutput

out)
throws

IOException

,

UnsupportedOperationException

Save this MLet's contents to the given

ObjectOutput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the written data.

The format of the written data is not specified, but if
an implementation supports

writeExternal(java.io.ObjectOutput)

it must
also support

readExternal(java.io.ObjectInput)

in such a way that what is
written by the former can be read by the latter.

Save this MLet's contents to the given

ObjectOutput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the written data.

The format of the written data is not specified, but if
an implementation supports

writeExternal(java.io.ObjectOutput)

it must
also support

readExternal(java.io.ObjectInput)

in such a way that what is
written by the former can be read by the latter.

readExternal

```java
public void readExternal​(
ObjectInput
in)
throws
IOException
,

ClassNotFoundException
,

UnsupportedOperationException
```

Restore this MLet's contents from the given

ObjectInput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the read data.

The format of the read data is not specified, but if an
implementation supports

readExternal(java.io.ObjectInput)

it must also
support

writeExternal(java.io.ObjectOutput)

in such a way that what is
written by the latter can be read by the former.

**Specified by:** readExternal

in interface

Externalizable
**Parameters:** in

- The object input stream to read from.
**Throws:** IOException

- if a problem occurred while reading.
**Throws:** ClassNotFoundException

- if the class for the object
being restored cannot be found.
**Throws:** UnsupportedOperationException

- if this
implementation does not support this operation.

---

#### readExternal

public void readExternal​(

ObjectInput

in)
throws

IOException

,

ClassNotFoundException

,

UnsupportedOperationException

Restore this MLet's contents from the given

ObjectInput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the read data.

The format of the read data is not specified, but if an
implementation supports

readExternal(java.io.ObjectInput)

it must also
support

writeExternal(java.io.ObjectOutput)

in such a way that what is
written by the latter can be read by the former.

Restore this MLet's contents from the given

ObjectInput

.
Not all implementations support this method. Those that do not
throw

UnsupportedOperationException

. A subclass may
override this method to support it or to change the format of
the read data.

The format of the read data is not specified, but if an
implementation supports

readExternal(java.io.ObjectInput)

it must also
support

writeExternal(java.io.ObjectOutput)

in such a way that what is
written by the latter can be read by the former.

loadClass

```java
public
Class
<?> loadClass​(
String
name,

ClassLoaderRepository
clr)
throws
ClassNotFoundException
```

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs. The given
ClassLoaderRepository can be null, in which case a

ClassNotFoundException

occurs immediately if the class is not
found in this MLet's URLs.

**Parameters:** name

- The name of the class we want to load.
**Parameters:** clr

- The ClassLoaderRepository that will be used to search
for the given class, if it is not found in this
ClassLoader. May be null.
**Returns:** The resulting Class object.
**Throws:** ClassNotFoundException

- The specified class could not be
found in this ClassLoader nor in the given
ClassLoaderRepository.

---

#### loadClass

public

Class

<?> loadClass​(

String

name,

ClassLoaderRepository

clr)
throws

ClassNotFoundException

Load a class, using the given

ClassLoaderRepository

if
the class is not found in this MLet's URLs. The given
ClassLoaderRepository can be null, in which case a

ClassNotFoundException

occurs immediately if the class is not
found in this MLet's URLs.

findClass

```java
protected
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

This is the main method for class loaders that is being redefined.

**Overrides:** findClass

in class

URLClassLoader
**Parameters:** name

- The name of the class.
**Returns:** The resulting Class object.
**Throws:** ClassNotFoundException

- The specified class could not be
found.

---

#### findClass

protected

Class

<?> findClass​(

String

name)
throws

ClassNotFoundException

This is the main method for class loaders that is being redefined.

findLibrary

```java
protected
String
findLibrary​(
String
libname)
```

Returns the absolute path name of a native library. The VM
invokes this method to locate the native libraries that belong
to classes loaded with this class loader. Libraries are
searched in the JAR files using first just the native library
name and if not found the native library name together with
the architecture-specific path name
(

OSName/OSArch/OSVersion/lib/nativelibname

), i.e.

the library stat on Solaris SPARC 5.7 will be searched in the JAR file as:

- libstat.so

SunOS/sparc/5.7/lib/libstat.so

the library stat on Windows NT 4.0 will be searched in the JAR file as:

- stat.dll

WindowsNT/x86/4.0/lib/stat.dll

More specifically, let

nativelibname

be the result of

System.mapLibraryName

(libname)

. Then the following names are
searched in the JAR files, in order:

nativelibname

<os.name>/<os.arch>/<os.version>/lib/

nativelibname

where

<X>

means

System.getProperty(X)

with any
spaces in the result removed, and

/

stands for the
file separator character (

File.separator

).

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

**Overrides:** findLibrary

in class

ClassLoader
**Parameters:** libname

- The library name.
**Returns:** The absolute path of the native library.
**See Also:** System.loadLibrary(String)

,

System.mapLibraryName(String)

---

#### findLibrary

protected

String

findLibrary​(

String

libname)

Returns the absolute path name of a native library. The VM
invokes this method to locate the native libraries that belong
to classes loaded with this class loader. Libraries are
searched in the JAR files using first just the native library
name and if not found the native library name together with
the architecture-specific path name
(

OSName/OSArch/OSVersion/lib/nativelibname

), i.e.

the library stat on Solaris SPARC 5.7 will be searched in the JAR file as:

- libstat.so

SunOS/sparc/5.7/lib/libstat.so

the library stat on Windows NT 4.0 will be searched in the JAR file as:

- stat.dll

WindowsNT/x86/4.0/lib/stat.dll

More specifically, let

nativelibname

be the result of

System.mapLibraryName

(libname)

. Then the following names are
searched in the JAR files, in order:

nativelibname

<os.name>/<os.arch>/<os.version>/lib/

nativelibname

where

<X>

means

System.getProperty(X)

with any
spaces in the result removed, and

/

stands for the
file separator character (

File.separator

).

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

the library stat on Solaris SPARC 5.7 will be searched in the JAR file as:

- libstat.so

SunOS/sparc/5.7/lib/libstat.so

the library stat on Windows NT 4.0 will be searched in the JAR file as:

- stat.dll

WindowsNT/x86/4.0/lib/stat.dll

More specifically, let

nativelibname

be the result of

System.mapLibraryName

(libname)

. Then the following names are
searched in the JAR files, in order:

nativelibname

<os.name>/<os.arch>/<os.version>/lib/

nativelibname

where

<X>

means

System.getProperty(X)

with any
spaces in the result removed, and

/

stands for the
file separator character (

File.separator

).

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

libstat.so

SunOS/sparc/5.7/lib/libstat.so

stat.dll

WindowsNT/x86/4.0/lib/stat.dll

More specifically, let

nativelibname

be the result of

System.mapLibraryName

(libname)

. Then the following names are
searched in the JAR files, in order:

nativelibname

<os.name>/<os.arch>/<os.version>/lib/

nativelibname

where

<X>

means

System.getProperty(X)

with any
spaces in the result removed, and

/

stands for the
file separator character (

File.separator

).

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

If this method returns

null

, i.e. the libraries
were not found in any of the JAR files loaded with this class
loader, the VM searches the library along the path specified
as the

java.library.path

property.

check

```java
protected
URL
check​(
String
version,

URL
codebase,

String
jarfile,

MLetContent
mlet)
throws
Exception
```

This method is to be overridden when extending this service to
support caching and versioning. It is called from

getMBeansFromURL

when the version,
codebase, and jarfile have been extracted from the MLet file,
and can be used to verify that it is all right to load the
given MBean, or to replace the given URL with a different one.

The default implementation of this method returns

codebase

unchanged.

**Parameters:** version

- The version number of the

.jar

file stored locally.
**Parameters:** codebase

- The base URL of the remote

.jar

file.
**Parameters:** jarfile

- The name of the

.jar

file to be loaded.
**Parameters:** mlet

- The

MLetContent

instance that
represents the

MLET

tag.
**Returns:** the codebase to use for the loaded MBean. The returned
value should not be null.
**Throws:** Exception

- if the MBean is not to be loaded for some
reason. The exception will be added to the set returned by

getMBeansFromURL

.

---

#### check

protected

URL

check​(

String

version,

URL

codebase,

String

jarfile,

MLetContent

mlet)
throws

Exception

This method is to be overridden when extending this service to
support caching and versioning. It is called from

getMBeansFromURL

when the version,
codebase, and jarfile have been extracted from the MLet file,
and can be used to verify that it is all right to load the
given MBean, or to replace the given URL with a different one.

The default implementation of this method returns

codebase

unchanged.

This method is to be overridden when extending this service to
support caching and versioning. It is called from

getMBeansFromURL

when the version,
codebase, and jarfile have been extracted from the MLet file,
and can be used to verify that it is all right to load the
given MBean, or to replace the given URL with a different one.

The default implementation of this method returns

codebase

unchanged.

---

