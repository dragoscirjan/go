package greeter

import (
	"testing"
)

func TestHello(t *testing.T) {
	tests := []struct {
		name        string
		input       string
		want        string
		wantErr     bool
		expectedErr error
	}{
		{
			name:    "valid name",
			input:   "World",
			want:    "Hello, World!",
			wantErr: false,
		},
		{
			name:    "name with spaces",
			input:   "John Doe",
			want:    "Hello, John Doe!",
			wantErr: false,
		},
		{
			name:    "name with leading/trailing whitespace",
			input:   "  Alice  ",
			want:    "Hello, Alice!",
			wantErr: false,
		},
		{
			name:        "empty string",
			input:       "",
			want:        "",
			wantErr:     true,
			expectedErr: ErrEmptyName,
		},
		{
			name:        "whitespace only",
			input:       "   ",
			want:        "",
			wantErr:     true,
			expectedErr: ErrEmptyName,
		},
		{
			name:        "tabs only",
			input:       "\t\t",
			want:        "",
			wantErr:     true,
			expectedErr: ErrEmptyName,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := Hello(tt.input)
			if (err != nil) != tt.wantErr {
				t.Errorf("Hello() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if tt.wantErr && err != tt.expectedErr {
				t.Errorf("Hello() error = %v, expectedErr %v", err, tt.expectedErr)
				return
			}
			if got != tt.want {
				t.Errorf("Hello() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGoodbye(t *testing.T) {
	tests := []struct {
		name        string
		input       string
		want        string
		wantErr     bool
		expectedErr error
	}{
		{
			name:    "valid name",
			input:   "World",
			want:    "Goodbye, World!",
			wantErr: false,
		},
		{
			name:    "name with spaces",
			input:   "John Doe",
			want:    "Goodbye, John Doe!",
			wantErr: false,
		},
		{
			name:    "name with leading/trailing whitespace",
			input:   "  Alice  ",
			want:    "Goodbye, Alice!",
			wantErr: false,
		},
		{
			name:        "empty string",
			input:       "",
			want:        "",
			wantErr:     true,
			expectedErr: ErrEmptyName,
		},
		{
			name:        "whitespace only",
			input:       "   ",
			want:        "",
			wantErr:     true,
			expectedErr: ErrEmptyName,
		},
		{
			name:        "tabs only",
			input:       "\t\t",
			want:        "",
			wantErr:     true,
			expectedErr: ErrEmptyName,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := Goodbye(tt.input)
			if (err != nil) != tt.wantErr {
				t.Errorf("Goodbye() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if tt.wantErr && err != tt.expectedErr {
				t.Errorf("Goodbye() error = %v, expectedErr %v", err, tt.expectedErr)
				return
			}
			if got != tt.want {
				t.Errorf("Goodbye() = %v, want %v", got, tt.want)
			}
		})
	}
}

// Benchmark tests
func BenchmarkHello(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, _ = Hello("World")
	}
}

func BenchmarkGoodbye(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, _ = Goodbye("World")
	}
}
