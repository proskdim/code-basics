result = hello()
expected = 'Hello, World!'
if result != expected
  puts "Получено: #{expected}, ожидалось: #{result}"
  exit 1
end
puts 'OK'
