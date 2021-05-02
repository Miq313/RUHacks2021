// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: tensorflow/core/protobuf/data/experimental/service_config.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3009000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3009002 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[2]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto;
namespace tensorflow {
namespace data {
namespace experimental {
class DispatcherConfig;
class DispatcherConfigDefaultTypeInternal;
extern DispatcherConfigDefaultTypeInternal _DispatcherConfig_default_instance_;
class WorkerConfig;
class WorkerConfigDefaultTypeInternal;
extern WorkerConfigDefaultTypeInternal _WorkerConfig_default_instance_;
}  // namespace experimental
}  // namespace data
}  // namespace tensorflow
PROTOBUF_NAMESPACE_OPEN
template<> ::tensorflow::data::experimental::DispatcherConfig* Arena::CreateMaybeMessage<::tensorflow::data::experimental::DispatcherConfig>(Arena*);
template<> ::tensorflow::data::experimental::WorkerConfig* Arena::CreateMaybeMessage<::tensorflow::data::experimental::WorkerConfig>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace tensorflow {
namespace data {
namespace experimental {

// ===================================================================

class DispatcherConfig :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:tensorflow.data.experimental.DispatcherConfig) */ {
 public:
  DispatcherConfig();
  virtual ~DispatcherConfig();

  DispatcherConfig(const DispatcherConfig& from);
  DispatcherConfig(DispatcherConfig&& from) noexcept
    : DispatcherConfig() {
    *this = ::std::move(from);
  }

  inline DispatcherConfig& operator=(const DispatcherConfig& from) {
    CopyFrom(from);
    return *this;
  }
  inline DispatcherConfig& operator=(DispatcherConfig&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const DispatcherConfig& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const DispatcherConfig* internal_default_instance() {
    return reinterpret_cast<const DispatcherConfig*>(
               &_DispatcherConfig_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(DispatcherConfig& a, DispatcherConfig& b) {
    a.Swap(&b);
  }
  inline void Swap(DispatcherConfig* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline DispatcherConfig* New() const final {
    return CreateMaybeMessage<DispatcherConfig>(nullptr);
  }

  DispatcherConfig* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<DispatcherConfig>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const DispatcherConfig& from);
  void MergeFrom(const DispatcherConfig& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(DispatcherConfig* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "tensorflow.data.experimental.DispatcherConfig";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto);
    return ::descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kProtocolFieldNumber = 2,
    kWorkDirFieldNumber = 3,
    kPortFieldNumber = 1,
    kJobGcCheckIntervalMsFieldNumber = 5,
    kJobGcTimeoutMsFieldNumber = 6,
    kFaultTolerantModeFieldNumber = 4,
  };
  // string protocol = 2;
  void clear_protocol();
  const std::string& protocol() const;
  void set_protocol(const std::string& value);
  void set_protocol(std::string&& value);
  void set_protocol(const char* value);
  void set_protocol(const char* value, size_t size);
  std::string* mutable_protocol();
  std::string* release_protocol();
  void set_allocated_protocol(std::string* protocol);

  // string work_dir = 3;
  void clear_work_dir();
  const std::string& work_dir() const;
  void set_work_dir(const std::string& value);
  void set_work_dir(std::string&& value);
  void set_work_dir(const char* value);
  void set_work_dir(const char* value, size_t size);
  std::string* mutable_work_dir();
  std::string* release_work_dir();
  void set_allocated_work_dir(std::string* work_dir);

  // int64 port = 1;
  void clear_port();
  ::PROTOBUF_NAMESPACE_ID::int64 port() const;
  void set_port(::PROTOBUF_NAMESPACE_ID::int64 value);

  // int64 job_gc_check_interval_ms = 5;
  void clear_job_gc_check_interval_ms();
  ::PROTOBUF_NAMESPACE_ID::int64 job_gc_check_interval_ms() const;
  void set_job_gc_check_interval_ms(::PROTOBUF_NAMESPACE_ID::int64 value);

  // int64 job_gc_timeout_ms = 6;
  void clear_job_gc_timeout_ms();
  ::PROTOBUF_NAMESPACE_ID::int64 job_gc_timeout_ms() const;
  void set_job_gc_timeout_ms(::PROTOBUF_NAMESPACE_ID::int64 value);

  // bool fault_tolerant_mode = 4;
  void clear_fault_tolerant_mode();
  bool fault_tolerant_mode() const;
  void set_fault_tolerant_mode(bool value);

  // @@protoc_insertion_point(class_scope:tensorflow.data.experimental.DispatcherConfig)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr protocol_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr work_dir_;
  ::PROTOBUF_NAMESPACE_ID::int64 port_;
  ::PROTOBUF_NAMESPACE_ID::int64 job_gc_check_interval_ms_;
  ::PROTOBUF_NAMESPACE_ID::int64 job_gc_timeout_ms_;
  bool fault_tolerant_mode_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto;
};
// -------------------------------------------------------------------

class WorkerConfig :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:tensorflow.data.experimental.WorkerConfig) */ {
 public:
  WorkerConfig();
  virtual ~WorkerConfig();

  WorkerConfig(const WorkerConfig& from);
  WorkerConfig(WorkerConfig&& from) noexcept
    : WorkerConfig() {
    *this = ::std::move(from);
  }

  inline WorkerConfig& operator=(const WorkerConfig& from) {
    CopyFrom(from);
    return *this;
  }
  inline WorkerConfig& operator=(WorkerConfig&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const WorkerConfig& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const WorkerConfig* internal_default_instance() {
    return reinterpret_cast<const WorkerConfig*>(
               &_WorkerConfig_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(WorkerConfig& a, WorkerConfig& b) {
    a.Swap(&b);
  }
  inline void Swap(WorkerConfig* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline WorkerConfig* New() const final {
    return CreateMaybeMessage<WorkerConfig>(nullptr);
  }

  WorkerConfig* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<WorkerConfig>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const WorkerConfig& from);
  void MergeFrom(const WorkerConfig& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(WorkerConfig* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "tensorflow.data.experimental.WorkerConfig";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto);
    return ::descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kProtocolFieldNumber = 2,
    kDispatcherAddressFieldNumber = 3,
    kWorkerAddressFieldNumber = 4,
    kPortFieldNumber = 1,
    kHeartbeatIntervalMsFieldNumber = 5,
    kDispatcherTimeoutMsFieldNumber = 6,
  };
  // string protocol = 2;
  void clear_protocol();
  const std::string& protocol() const;
  void set_protocol(const std::string& value);
  void set_protocol(std::string&& value);
  void set_protocol(const char* value);
  void set_protocol(const char* value, size_t size);
  std::string* mutable_protocol();
  std::string* release_protocol();
  void set_allocated_protocol(std::string* protocol);

  // string dispatcher_address = 3;
  void clear_dispatcher_address();
  const std::string& dispatcher_address() const;
  void set_dispatcher_address(const std::string& value);
  void set_dispatcher_address(std::string&& value);
  void set_dispatcher_address(const char* value);
  void set_dispatcher_address(const char* value, size_t size);
  std::string* mutable_dispatcher_address();
  std::string* release_dispatcher_address();
  void set_allocated_dispatcher_address(std::string* dispatcher_address);

  // string worker_address = 4;
  void clear_worker_address();
  const std::string& worker_address() const;
  void set_worker_address(const std::string& value);
  void set_worker_address(std::string&& value);
  void set_worker_address(const char* value);
  void set_worker_address(const char* value, size_t size);
  std::string* mutable_worker_address();
  std::string* release_worker_address();
  void set_allocated_worker_address(std::string* worker_address);

  // int64 port = 1;
  void clear_port();
  ::PROTOBUF_NAMESPACE_ID::int64 port() const;
  void set_port(::PROTOBUF_NAMESPACE_ID::int64 value);

  // int64 heartbeat_interval_ms = 5;
  void clear_heartbeat_interval_ms();
  ::PROTOBUF_NAMESPACE_ID::int64 heartbeat_interval_ms() const;
  void set_heartbeat_interval_ms(::PROTOBUF_NAMESPACE_ID::int64 value);

  // int64 dispatcher_timeout_ms = 6;
  void clear_dispatcher_timeout_ms();
  ::PROTOBUF_NAMESPACE_ID::int64 dispatcher_timeout_ms() const;
  void set_dispatcher_timeout_ms(::PROTOBUF_NAMESPACE_ID::int64 value);

  // @@protoc_insertion_point(class_scope:tensorflow.data.experimental.WorkerConfig)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr protocol_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr dispatcher_address_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr worker_address_;
  ::PROTOBUF_NAMESPACE_ID::int64 port_;
  ::PROTOBUF_NAMESPACE_ID::int64 heartbeat_interval_ms_;
  ::PROTOBUF_NAMESPACE_ID::int64 dispatcher_timeout_ms_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// DispatcherConfig

// int64 port = 1;
inline void DispatcherConfig::clear_port() {
  port_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 DispatcherConfig::port() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.DispatcherConfig.port)
  return port_;
}
inline void DispatcherConfig::set_port(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  port_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.DispatcherConfig.port)
}

// string protocol = 2;
inline void DispatcherConfig::clear_protocol() {
  protocol_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline const std::string& DispatcherConfig::protocol() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.DispatcherConfig.protocol)
  return protocol_.GetNoArena();
}
inline void DispatcherConfig::set_protocol(const std::string& value) {
  
  protocol_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.DispatcherConfig.protocol)
}
inline void DispatcherConfig::set_protocol(std::string&& value) {
  
  protocol_.SetNoArena(
    &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:tensorflow.data.experimental.DispatcherConfig.protocol)
}
inline void DispatcherConfig::set_protocol(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  protocol_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:tensorflow.data.experimental.DispatcherConfig.protocol)
}
inline void DispatcherConfig::set_protocol(const char* value, size_t size) {
  
  protocol_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:tensorflow.data.experimental.DispatcherConfig.protocol)
}
inline std::string* DispatcherConfig::mutable_protocol() {
  
  // @@protoc_insertion_point(field_mutable:tensorflow.data.experimental.DispatcherConfig.protocol)
  return protocol_.MutableNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline std::string* DispatcherConfig::release_protocol() {
  // @@protoc_insertion_point(field_release:tensorflow.data.experimental.DispatcherConfig.protocol)
  
  return protocol_.ReleaseNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline void DispatcherConfig::set_allocated_protocol(std::string* protocol) {
  if (protocol != nullptr) {
    
  } else {
    
  }
  protocol_.SetAllocatedNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), protocol);
  // @@protoc_insertion_point(field_set_allocated:tensorflow.data.experimental.DispatcherConfig.protocol)
}

// string work_dir = 3;
inline void DispatcherConfig::clear_work_dir() {
  work_dir_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline const std::string& DispatcherConfig::work_dir() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.DispatcherConfig.work_dir)
  return work_dir_.GetNoArena();
}
inline void DispatcherConfig::set_work_dir(const std::string& value) {
  
  work_dir_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.DispatcherConfig.work_dir)
}
inline void DispatcherConfig::set_work_dir(std::string&& value) {
  
  work_dir_.SetNoArena(
    &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:tensorflow.data.experimental.DispatcherConfig.work_dir)
}
inline void DispatcherConfig::set_work_dir(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  work_dir_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:tensorflow.data.experimental.DispatcherConfig.work_dir)
}
inline void DispatcherConfig::set_work_dir(const char* value, size_t size) {
  
  work_dir_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:tensorflow.data.experimental.DispatcherConfig.work_dir)
}
inline std::string* DispatcherConfig::mutable_work_dir() {
  
  // @@protoc_insertion_point(field_mutable:tensorflow.data.experimental.DispatcherConfig.work_dir)
  return work_dir_.MutableNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline std::string* DispatcherConfig::release_work_dir() {
  // @@protoc_insertion_point(field_release:tensorflow.data.experimental.DispatcherConfig.work_dir)
  
  return work_dir_.ReleaseNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline void DispatcherConfig::set_allocated_work_dir(std::string* work_dir) {
  if (work_dir != nullptr) {
    
  } else {
    
  }
  work_dir_.SetAllocatedNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), work_dir);
  // @@protoc_insertion_point(field_set_allocated:tensorflow.data.experimental.DispatcherConfig.work_dir)
}

// bool fault_tolerant_mode = 4;
inline void DispatcherConfig::clear_fault_tolerant_mode() {
  fault_tolerant_mode_ = false;
}
inline bool DispatcherConfig::fault_tolerant_mode() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.DispatcherConfig.fault_tolerant_mode)
  return fault_tolerant_mode_;
}
inline void DispatcherConfig::set_fault_tolerant_mode(bool value) {
  
  fault_tolerant_mode_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.DispatcherConfig.fault_tolerant_mode)
}

// int64 job_gc_check_interval_ms = 5;
inline void DispatcherConfig::clear_job_gc_check_interval_ms() {
  job_gc_check_interval_ms_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 DispatcherConfig::job_gc_check_interval_ms() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.DispatcherConfig.job_gc_check_interval_ms)
  return job_gc_check_interval_ms_;
}
inline void DispatcherConfig::set_job_gc_check_interval_ms(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  job_gc_check_interval_ms_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.DispatcherConfig.job_gc_check_interval_ms)
}

// int64 job_gc_timeout_ms = 6;
inline void DispatcherConfig::clear_job_gc_timeout_ms() {
  job_gc_timeout_ms_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 DispatcherConfig::job_gc_timeout_ms() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.DispatcherConfig.job_gc_timeout_ms)
  return job_gc_timeout_ms_;
}
inline void DispatcherConfig::set_job_gc_timeout_ms(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  job_gc_timeout_ms_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.DispatcherConfig.job_gc_timeout_ms)
}

// -------------------------------------------------------------------

// WorkerConfig

// int64 port = 1;
inline void WorkerConfig::clear_port() {
  port_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 WorkerConfig::port() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.WorkerConfig.port)
  return port_;
}
inline void WorkerConfig::set_port(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  port_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.WorkerConfig.port)
}

// string protocol = 2;
inline void WorkerConfig::clear_protocol() {
  protocol_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline const std::string& WorkerConfig::protocol() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.WorkerConfig.protocol)
  return protocol_.GetNoArena();
}
inline void WorkerConfig::set_protocol(const std::string& value) {
  
  protocol_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.WorkerConfig.protocol)
}
inline void WorkerConfig::set_protocol(std::string&& value) {
  
  protocol_.SetNoArena(
    &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:tensorflow.data.experimental.WorkerConfig.protocol)
}
inline void WorkerConfig::set_protocol(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  protocol_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:tensorflow.data.experimental.WorkerConfig.protocol)
}
inline void WorkerConfig::set_protocol(const char* value, size_t size) {
  
  protocol_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:tensorflow.data.experimental.WorkerConfig.protocol)
}
inline std::string* WorkerConfig::mutable_protocol() {
  
  // @@protoc_insertion_point(field_mutable:tensorflow.data.experimental.WorkerConfig.protocol)
  return protocol_.MutableNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline std::string* WorkerConfig::release_protocol() {
  // @@protoc_insertion_point(field_release:tensorflow.data.experimental.WorkerConfig.protocol)
  
  return protocol_.ReleaseNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline void WorkerConfig::set_allocated_protocol(std::string* protocol) {
  if (protocol != nullptr) {
    
  } else {
    
  }
  protocol_.SetAllocatedNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), protocol);
  // @@protoc_insertion_point(field_set_allocated:tensorflow.data.experimental.WorkerConfig.protocol)
}

// string dispatcher_address = 3;
inline void WorkerConfig::clear_dispatcher_address() {
  dispatcher_address_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline const std::string& WorkerConfig::dispatcher_address() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
  return dispatcher_address_.GetNoArena();
}
inline void WorkerConfig::set_dispatcher_address(const std::string& value) {
  
  dispatcher_address_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
}
inline void WorkerConfig::set_dispatcher_address(std::string&& value) {
  
  dispatcher_address_.SetNoArena(
    &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
}
inline void WorkerConfig::set_dispatcher_address(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  dispatcher_address_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
}
inline void WorkerConfig::set_dispatcher_address(const char* value, size_t size) {
  
  dispatcher_address_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
}
inline std::string* WorkerConfig::mutable_dispatcher_address() {
  
  // @@protoc_insertion_point(field_mutable:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
  return dispatcher_address_.MutableNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline std::string* WorkerConfig::release_dispatcher_address() {
  // @@protoc_insertion_point(field_release:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
  
  return dispatcher_address_.ReleaseNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline void WorkerConfig::set_allocated_dispatcher_address(std::string* dispatcher_address) {
  if (dispatcher_address != nullptr) {
    
  } else {
    
  }
  dispatcher_address_.SetAllocatedNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), dispatcher_address);
  // @@protoc_insertion_point(field_set_allocated:tensorflow.data.experimental.WorkerConfig.dispatcher_address)
}

// string worker_address = 4;
inline void WorkerConfig::clear_worker_address() {
  worker_address_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline const std::string& WorkerConfig::worker_address() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.WorkerConfig.worker_address)
  return worker_address_.GetNoArena();
}
inline void WorkerConfig::set_worker_address(const std::string& value) {
  
  worker_address_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.WorkerConfig.worker_address)
}
inline void WorkerConfig::set_worker_address(std::string&& value) {
  
  worker_address_.SetNoArena(
    &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:tensorflow.data.experimental.WorkerConfig.worker_address)
}
inline void WorkerConfig::set_worker_address(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  worker_address_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:tensorflow.data.experimental.WorkerConfig.worker_address)
}
inline void WorkerConfig::set_worker_address(const char* value, size_t size) {
  
  worker_address_.SetNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:tensorflow.data.experimental.WorkerConfig.worker_address)
}
inline std::string* WorkerConfig::mutable_worker_address() {
  
  // @@protoc_insertion_point(field_mutable:tensorflow.data.experimental.WorkerConfig.worker_address)
  return worker_address_.MutableNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline std::string* WorkerConfig::release_worker_address() {
  // @@protoc_insertion_point(field_release:tensorflow.data.experimental.WorkerConfig.worker_address)
  
  return worker_address_.ReleaseNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
inline void WorkerConfig::set_allocated_worker_address(std::string* worker_address) {
  if (worker_address != nullptr) {
    
  } else {
    
  }
  worker_address_.SetAllocatedNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), worker_address);
  // @@protoc_insertion_point(field_set_allocated:tensorflow.data.experimental.WorkerConfig.worker_address)
}

// int64 heartbeat_interval_ms = 5;
inline void WorkerConfig::clear_heartbeat_interval_ms() {
  heartbeat_interval_ms_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 WorkerConfig::heartbeat_interval_ms() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.WorkerConfig.heartbeat_interval_ms)
  return heartbeat_interval_ms_;
}
inline void WorkerConfig::set_heartbeat_interval_ms(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  heartbeat_interval_ms_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.WorkerConfig.heartbeat_interval_ms)
}

// int64 dispatcher_timeout_ms = 6;
inline void WorkerConfig::clear_dispatcher_timeout_ms() {
  dispatcher_timeout_ms_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 WorkerConfig::dispatcher_timeout_ms() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.experimental.WorkerConfig.dispatcher_timeout_ms)
  return dispatcher_timeout_ms_;
}
inline void WorkerConfig::set_dispatcher_timeout_ms(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  dispatcher_timeout_ms_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.experimental.WorkerConfig.dispatcher_timeout_ms)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace experimental
}  // namespace data
}  // namespace tensorflow

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprotobuf_2fdata_2fexperimental_2fservice_5fconfig_2eproto
